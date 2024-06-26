# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal 
# to or lower than 1000. Otherwise, return their sum.

def multiplicationOrSumTwoNumber(number1, number2):
  multiplication = number1 * number2

  if(multiplication > 1000):
    return print(number1 + number2)
  
  return print(multiplication)


multiplicationOrSumTwoNumber(40, 30)