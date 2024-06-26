# Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that 
# are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# Solution 1
word = input("Enter word: ")
print("\nOriginal string: ", word, "\n")

# size = len(word)

# for i in range(0, size -1, 2):
#   print(word[i])

# Solution 2

x = list(word)
for i in x[0::2]:
  print(i)
