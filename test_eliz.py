import pytest
import calculator
from calculator import *
from pytest import approx

# Test addition
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test subtraction
def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

# Test multiplication
def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 4) == -8

# Test division
def test_division():
    assert divide(6, 2) == 3
    assert divide(10, 3) == pytest.approx(3.3333333333333335)
    assert divide(5, 0) == "Cannot divide by 0"

# Additional test cases
def test_addition_large_numbers():
    result = add(1000000, 2000000)
    assert result == 3000000
    assert isinstance(result, int)

def test_subtraction_negative_result():
    result = subtract(3, 5)
    assert result == -2
    assert isinstance(result, int)

def test_division_float_result():
    result = divide(7, 2)
    assert result == pytest.approx(3.5)
    assert isinstance(result, float)

def test_division_rounding():
    result = divide(10, 3)
    assert result == pytest.approx(3.333, abs=0.001)

#def test_divide_by_zero_exception():
#    with pytest.raises(ZeroDivisionError):
#        divide(5, 0)


# Additional test cases
def test_addition_large_numbers():
    result = add(1000000, 2000000)
    assert result == 3000000
    assert isinstance(result, int)

def test_subtraction_negative_result():
    result = subtract(3, 5)
    assert result == -2
    assert isinstance(result, int)

def test_division_float_result():
    result = divide(7, 2)
    assert result == pytest.approx(3.5)
    assert isinstance(result, float)

def test_division_rounding():
    result = divide(10, 3)
    assert result == pytest.approx(3.333, abs=0.001)

#def test_divide_by_zero_exception ():
#    with pytest.raises(ZeroDivisionError):
#        divide(5, 0)

#def test_divide_by_zero():
#    num1 = 2
#    num2 = 0
#    operator = "/"

#    with pytest.raises(ZeroDivisionError):
#        divide(10, 3)

# Additional complex scenarios
#def test_complex_operations():
#    result = add(5, multiply(2, subtract(8, divide(10, 2)))
#    assert result == 14

# handles addition
def test_addition():
  result = add (2,3)
  assert result == 5

# handles subtraction
def test_subtraction():
  assert subtract(10, 1) == 9

# handles multiplication
def test_multiply():
  assert multiply(1, 10) == 10

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(1, 0) == "Cannot divide by 0"
  assert divide(10, 3) == 10/3
  assert divide(99,2) == 49.5

def test_get_num(monkeypatch):
  # Mock user input for valid integer
  monkeypatch.setattr('builtins.input', lambda _: "42")
  assert get_num("Enter a number: ") == 42

  # Mock user input for invalid input (non-integer)
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  assert get_num(
      "Enter a number: ") == "Please enter a valid integer"

def test_get_selection(monkeypatch):
    # Mock user input for valid selection
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_selection() == 3

    # Mock user input for invalid selection
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(ValueError):
        get_selection()

# Handles division by a negative number
def test_divide_negative():
  assert divide(10, -2) == -5
  assert divide(-10, -2) == 5
  assert divide(-10, 2) == -5

# Handles division by a positive number
def test_divide_positive():
  assert divide(10, 2) == 5

# Handles division by a floating-point number
def test_divide_float():
  assert divide(10, 3) == 10/3

# Handles division by zero with negative dividend
def test_divide_zero_negative():
  assert divide(-10, 0) == "Cannot divide by 0"

# Handles division by zero with positive dividend
def test_divide_zero_positive():
  assert divide(10, 0) == "Cannot divide by 0"

# Gets a selection from user input with valid range
def test_get_selection_valid_range(monkeypatch):
  # Mock user input for valid selection
  monkeypatch.setattr('builtins.input', lambda _: "3")
  assert get_selection() == 3

  # Mock user input for invalid selection
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  with pytest.raises(ValueError):
      get_selection()

# Handles division by zero with zero dividend
def test_divide_zero_zero():
  assert divide(0, 0) == "Cannot divide by 0"
  
  
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 5), (-2, -3, -5), (2, -3, -1)])
def test_param_add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult

# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 6), (-2, -3, 6), (2, -3, -6)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult

# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(21, 3, 7), (-21, -3, 7), (-21, 3, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
    assert result == expectedResult

# Test Calculator does not take in more than 3 values

# Test Calculator when double 0 values entered
def test_doubleZeroInput():
    result = calculator.subtract(0, 0)
    assert result == 0

