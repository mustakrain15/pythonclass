#exception handelling 
# try:
#     #code
# except Exception:
#     #code
# except Exception:
#     #code
# else:
#     #co
# finally:
    #code 


# firstnumber=int(input("enter the first number"))
# secondnumber=int(input("enter the second number "))
# print(firstnumber+secondnumber)

try:
    a=int(input("enater the f number"))
    b=int(input("enter the second number"))
except ValueError:
    print("canot not convert thew eror")
else:
    print(a+b)

