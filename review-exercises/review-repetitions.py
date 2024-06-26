# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print 
# the sum of the current and previous number.

def sumCurrentNumberAndPreviousNumber():
  prev = 0
  for n in range(10):
    if(n > 0):
      prev = n - 1
    
    sum = n + prev
    print(sum)

sumCurrentNumberAndPreviousNumber()