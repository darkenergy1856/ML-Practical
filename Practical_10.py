# Use conditional statements and different type of loops based on simple example/

def check_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def print_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

def calculate_factorial(number):
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number - 1
    return factorial

score = int(input("Enter your score: "))
grade = check_grade(score)
print("Your grade is", grade)

number = int(input("Enter a number: "))
print_table(number)

factorial = calculate_factorial(number)
print("The factorial is", factorial)
