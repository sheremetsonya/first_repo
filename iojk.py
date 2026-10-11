while True:
    number1=float(input("введи перше число: "))
    operation=input("введи операцію (+, -, *, /, %, **): ")
    number2=float(input("введи друге число:"))
    if operation=="+":
       print("результат:", number1 + number2)
    elif operation=="-":
       print("результат:", number1 - number2)
    elif operation=="*":
       print("результат:", number1 * number2)
    elif operation=="%":
       result= number1 * number2 / 100
       print("результат:", result)
    elif operation=="**":
       result=number1 ** number2
       print("результат:", result)
    elif operation== "/":
       if number2 != 0:
          print("результат:", number1 / number2)
       else:
          print("помилка: на нуль ділити не можна!")
    else:
     print("невідома операція")
    again=input("хочеш порахувати ще раз? (так/ні):")
    if again.lower() !="так":
       break
print("дякую за використання калькулятора!")