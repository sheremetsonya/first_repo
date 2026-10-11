number1=float(input("введи перше число: "))
operation=input("введи операцію (+, -, *, /): ")
number2=float(input("введи друге число:"))
if operation=="+":
    print(number1 + number2)
elif operation=="-":
    print(number1 - number2)
elif operation=="*":
    print(number1 * number2)
elif operation== "/":
    print(number1 / number2)
else:
    print("невідома операція")