def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  try:
    return (num1 / num2)
  except ZeroDivisionError:
     return "Cannot divide by 0"

def get_num(text):
  try:
     return int(input(f"\n{text}"))
  except ValueError:
     return "Please enter a valid integer"

def get_selection():
  selection = int(input("\nSelect your calculator operations: \
                      \n1.Addition\
                      \n2.Subtraction\
                      \n3.Multiplication\
                      \n4.Division\n\n"))
  if selection not in (1, 2, 3, 4):
    raise ValueError
  return selection

