#! /usr/bin/env python3
# calculator.py
# A simple calculator program that performs basic arithmetic operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")   
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")