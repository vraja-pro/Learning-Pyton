
num1 = int(input("Write a number "))
todo = input("Pleae enter either + - / *" )
num2 = int(input("second number "))
while True:
       if todo == "+":
              result = num1 + num2
              break
       elif todo == "-":
              result = num1 - num2
              break
       elif todo == "/":
              result = num1 / num2
              break
       elif todo == "*":
              result = num1 * num2
              break
       else:
              print("wrong character")


print("your result is {0}".format(result))
