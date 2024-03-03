# Project: Calculator

# define functions that add, subtract multiply, divide and raises to power
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def power(n1, n2):
  return n1 ** n2

operators_dict = {'+': add, '-': subtract, '*': multiply, '/': divide, '**': power}
calculate = True
def calculator():
  calculate = True
  replay = True
  while replay:
    num1 = float(input("What is the first number? "))
    for sign in operators_dict:
      print(sign)
      
    while calculate:
      operator = input("Pick an operator: ")
      num2 =float(input("What is the next number? "))
    
      result = operators_dict[operator](num1, num2)
      
      print(f"{num1} {operator} {num2} = {result}")
    
      choice = input(f"do you want to calculate using {result} or start a new calculation? 'y' for yes or 'n' for no: ")
      if choice == 'y':
        num1 = result
      else:
        calculate = False
        
    choice2 = input("do you want to continue calculating or exit? 'y' for yes or 'n' for no: ")
    if choice2 == 'y':
      calculator()
    else:
        calculate = False
        replay = False

calculator()