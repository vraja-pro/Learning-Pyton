from calaulator_func import action, calculate

print("This is a Calculator")
num1 = int(input("Write first number "))
todo = input("Please enter either + - / * to result or exit press = > " )
if todo == "=":
       pass
else:
       num2 = input("another number or exit by = >")
       if num2 != "=":
              num2 = int(num2)
              result = calculate(num1,todo,num2)
              num1 = result

print("Your result is {0}".format(num1))


