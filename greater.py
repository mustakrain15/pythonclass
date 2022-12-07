number1=int(input("please enter the number1:"))
number2=int(input("please enter the number2:"))
number3=int(input("please enter the number3:"))
if number2<number1>number3:
    print(f" this is the greater number :{number1} ")
elif number3<number2>number1:
    print(f"this is grater nuimber:{number2}")
elif number1<number3<number2:
    print(f"this is greater number:{number3} ")
else:
    print("thank you")