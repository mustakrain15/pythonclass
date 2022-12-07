# # a=[]
# # for i in  range(2,30,2):
# #     a.append(i)
# # print(a)

# # a=[i for i in range (2,20,2)]
# print(a)


email=["1@gmail.com","2@gmail.com","3@gmail.com","4@outlook.com","5@yahoo.com","6@gmail.com","7@outmail.com","8@gmail.com"]
output=[]
for i in  email:
    if i.endswith("@gmail.com"):
       output.append(i)
print(output)

print((i for i in email if i.endswith("@gmail.com")))