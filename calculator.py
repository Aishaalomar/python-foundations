number1=input("Enter first number")
if not number1.isdigit():
    number1 = input("Wrong input try again")

number2=input("Enter second number")
if not number2.isdigit():
    number2=input("wrong input try again")
    
number1 = int(number1)
number2 = int(number2)

if operation=='+':
    answer = int(number1) + number2

elif operation=='-':
    answer =  number1 - number2

elif operation=='*':
    answer = number1 * number2

elif operation=='/':
    answer = number1/number2
else:
    print("Invalid input")

print("the answer is %s" %(answer))

