def action(num1):
    print("Result for now: {0}".format(num1))
    todo = input("Please enter either + - / * to result or exit press = > ")
    return todo

def calculate(num1,todo,num2):
    while True:
        if todo == "+":
            num1 += num2
            todo = action(num1)
            if todo == "=":
                break
            else:
                num2 = input("another number or exit by = >")
                if num2 == "=":
                    break
                else:
                    num2 = int(num2)
        elif todo == "-":
            num1 -= num2
            todo = action(num1)
            if todo == "=":
                break
            else:
                num2 = input("another number or exit by = >")
                if num2 == "=":
                    break
                else:
                    num2 = int(num2)
        elif todo == "/":
            if num1 != 0:
                num1 /= num2
                todo = action(num1)
                if todo == "=":
                    break
                else:
                    num2 = input("another number or exit by = >")
                    if num2 == "=":
                        break
                    else:
                        num2 = int(num2)
            else:
                print("Can't devide by 0, try again")
                num1 = int(input("Write a number "))
        elif todo == "*":
            result = num1 * num2
            todo = action(num1)
            if todo == "=":
                break
            else:
                num2 = input("another number or exit by = >")
                if num2 == "=":
                    break
                else:
                    num2 = int(num2)
        else:
            print("wrong character")
            todo = input("Please enter either + - / * or = to exit ")
    return(num1)
