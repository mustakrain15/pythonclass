# #def mustak():
# #    print("hellow ")
# #mustak()
# #mustak

# def sum(num1,num2):
#     total= num1 + num2
#     return total
# total_sum =sum(10,15)
# print(total_sum)    

# def profile(name,lsss,rollno):
#         print(f"name:{name}")
#         print(f"lsss:{lsss}")
#         print(f"rollno:{rollno}")
# profile("ram","ktm","958749")

# def total_sum(number1,number2):
#     total = number1 + number2
#     print(f"total:{total}")


def ram(*args):
    print(args)

ram(1,2,3,4,5)

def shamir(**kwargs):
    print(kwargs)

shamir(samir="fatha", usko_kam="fatha kam garne", uskoghar="mero ghar xeumah")



def mix_function(*args,kwargs):
    for i in args:
        print(i)
    print(kwargs.get("name"))

def multiple_of_num(num1,faramctor=5):
    return num1*faramctor

print(multiple_of_num(10))
