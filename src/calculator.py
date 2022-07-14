def add (num1,num2):
    return num1+num2
def subtract (num1,num2):
    return num1-num2
def multiply (num1,num2):
    return num1*num2
def divide (num1,num2):
    return num1/num2
operations={
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
        }

try:
    str1=input("enter the expression seperated by space:\n")
    li = str1.split()
    result=operations[li[1]](int(li[0]),int(li[2]))
    print(result)
    while 1:
        li=input("\n").split()
        if li[0] in operations:
            result=operations[li[0]](result,int(li[1]))
            print(result)
        elif li[0].lower() == 'n':
            break
        else:
            result=operations[li[1]](int(li[0]),int(li[2]))
            print(result)

except:
    print("Terminated - You have not entered the valid number")
