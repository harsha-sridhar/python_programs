def add (num1,num2):
    return num1+num2
def subtract (num1,num2):
    return num1-num2
def multiply (num1,num2):
    return num1*num2
def divide (num1,num2):
    return num1/num2
try:
    number1=int(input("enter the number :"))
    operations=['+','-','*','/']
    to_continue='y'
    result=0
    while to_continue == 'y':
        operator=input("choose the operations +, -, *, /\n")
        while operator not in operations:
            operator=input("enter one of the operation +, -, *, /\n")
            if operator in operations:
                break
        number2=int(input("enter the number :"))
        if operator == '+':
            result=add(number1,number2)
        elif operator == '-':
            result=subtract(number1,number2)
        elif operator == '*':
            result=multiply(number1,number2)
        elif operator == '-':
            result=divide(number1,number2)
        print(result)
        number1 = result
        to_continue = input("\n Do you want to continue? Y/N : ")
        if to_continue.lower()=='n':
            break
        elif to_continue.lower() not in ['y','n']:
            while to_continue not in ['y','n']:
                print("\nenter valid character")
                to_continue=input("\n Press Y or N").lower()
        else:
            to_continue='y'
except ValueError:
    print("Terminated - You have not entered the valid number")


