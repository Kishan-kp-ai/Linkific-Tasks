from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import faiss
import numpy as np
import io
import os

app = FastAPI(title="Simple RAG API")

# -----------------------------
# Load models
# -----------------------------

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
llm = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


# -----------------------------
# Store uploaded document
# -----------------------------

chunks = []
vector_db = None


# -----------------------------
# Extract text from files
# -----------------------------

def extract_text(filename, content):

    extension = os.path.splitext(filename)[1].lower()

    # TXT
    if extension == ".txt":
        return content.decode("utf-8", errors="ignore")

    # PDF
    elif extension == ".pdf":
        reader = PdfReader(io.BytesIO(content))

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    # DOCX
    elif extension == ".docx":
        document = Document(io.BytesIO(content))

        text = "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

        return text

    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Use TXT, PDF or DOCX."
        )


# -----------------------------
# Split document into chunks
# -----------------------------

def create_chunks(text, chunk_size=500):

    text = text.strip()

    if not text:
        return []

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


# -----------------------------
# Create FAISS database
# -----------------------------

def create_vector_database(document_chunks):

    embeddings = embedding_model.encode(
        document_chunks,
        normalize_embeddings=True
    )

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatIP(embeddings.shape[1])

    index.add(embeddings)

    return index


# -----------------------------
# Health check
# -----------------------------

@app.get("/health")
def health():

    return {
        "status": "API is running"
    }


# -----------------------------
# Upload document
# -----------------------------

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    global chunks
    global vector_db

    content = await file.read()

    # Check empty file
    if len(content) == 0:

        raise HTTPException(
            status_code=400,
            detail="File is empty."
        )

    # Check large files
    max_size = 10 * 1024 * 1024

    if len(content) > max_size:

        raise HTTPException(
            status_code=413,
            detail="File is too large. Maximum size is 10 MB."
        )

    # Extract text
    text = extract_text(
        file.filename,
        content
    )

    # Check empty document
    if not text.strip():

        raise HTTPException(
            status_code=400,
            detail="No readable text found in the document."
        )

    # Create chunks
    chunks = create_chunks(
        text,
        chunk_size=500
    )

    # Create vector database
    vector_db = create_vector_database(chunks)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks)
    }


# -----------------------------
# Ask question
# -----------------------------

@app.get("/ask")
def ask_question(question: str):

    global chunks
    global vector_db

    if vector_db is None:

        raise HTTPException(
            status_code=400,
            detail="Please upload a document first."
        )

    # Create question embedding
    question_embedding = embedding_model.encode(
        [question],
        normalize_embeddings=True
    )

    question_embedding = np.array(
        question_embedding
    ).astype("float32")

    # Retrieve top 2 chunks
    scores, indexes = vector_db.search(
        question_embedding,
        min(2, len(chunks))
    )

    retrieved_chunks = [
        chunks[i]
        for i in indexes[0]
        if i >= 0
    ]

    # Combine retrieved information
    context = "\n".join(retrieved_chunks)

    # Create prompt
    prompt = f"""
Answer the question using only the information provided below.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = llm.generate(
        **inputs,
        max_new_tokens=100
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": retrieved_chunks,
        "similarity_scores": scores[0].tolist()
    }