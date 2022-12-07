#print("hellow brodway")
#take user input  15 timesin int 
# main even odd duplicate 
# i=()
# num=input("enter the number")
# i=[i for num in range (15)]
# print(num)

main=[]
even=[]
odd=[]
duplicate=[]

for i in range (15):
    num =int(input("ENTER THE NUMBER"))
    if num in main:
        duplicate.append(num)
    else:
        if num % 2 ==0:
         even.append(num)
        else:
            odd.append(num)
    main.append(num)
print(f"main list:{main}")
print(f"even list:{even}")
print(f"odd list:{odd}")
print(f"duplicate list:{duplicate}")




