marks = float(input("Enter your marks: "))

if marks < 40:
    print("Fail")
elif marks < 60:
    print("Pass")
elif marks < 75:
    print("Good")
else:
    print("Excellent")

# Variables
name = "Kishan"
age = 21
marks = 85.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

 # Conditional statement
if marks >= 40:
    print("Student has passed")
else:
    print("Student has failed")

 # For loop
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

# While loop
count = 1

while count <= 5:
    print(count)
    count += 1

# Function
def greet(name):
    return "Hello " + name

print(greet("Kishan"))
