# # colors =["yellow","red","green","blue","yellow","orange","red"]
# # # remove=["yellow","red"]
# # output=[]
# # for i colours:
# #     colors.remove("red")    
# #     colors.remove("yellow")

# # print(output)


colors =["yellow","red","green","blue","yellow","orange","red" ]
new_list=[]
item_to_remove=[]
C1=input("enter the first colour you want to remove: ")
item_to_remove.append(C1)
c2=input("enter the second colour you want to remove:")
item_to_remove.append(c2)

for i in colors:
    if i not in item_to_remove:
        new_list.append(i)

print(new_list)



# colors =["yellow","red","green","blue","yellow","orange","red"]



# number=[1,2,3,4,5,6,7]
# number.remove(5)
# print(number)