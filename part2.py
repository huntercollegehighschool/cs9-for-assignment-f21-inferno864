"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

#write your code here
number = int(input("Enter a number: "))
cube = number
number2 = number
total = cube 
cube2 = 0
for i in range(number + 1, 1, -1): 
  cube2 = cube
  cube = cube2
  cube = number * number * number
  number -= 1 
  total = cube + cube2
  cube = total
  
print(total - number2)