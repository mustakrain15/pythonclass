# a={
#     "properties":{
#         "profile":{
#             "name":"ram",
#             "education":[
#                 {"collage":"abc","year":2018},
#                 {"collage":"xyz","year":2020},
#             ]
            

#             },
#             "follower": 10000,
#             "following": 100,
#         }
#     }
# # p=a.get("prooerties").get("profile")
# # print(p)

# name= a.get("properties").get("profile").get("name")
# followers=a.get("properties").get("follower")
# # following=a.get("properties").get("following")
# # print(f"Name:{name.capitalize()}")
# # print(f"follower: {followers}")
# # print(f"following :{following}")
# # education=a.get("properties").get("profile").get("education")
# # for education in education:
# #     collage =education.get("collage")
# #     year =education.get("year")
# #     print(f"education{year}:{collage.upper()}")




# # student score
# student_score = [
#     {"name":"Ram","score":80},
#     {"name":"shyam","score":70},
#     {"name":"hari","score":50}, 
#     {"name":"gita","score":30},
#     {"name":"jon","score":90},
#     {"name":"sid","score":40},
# ]

# out = []
# # print(student_score)
# for i in student_score:
#     score=i.get("score")
#     if score >= 40:
#         out.append(i)
    
# print(out)



colors =["yellow","red","green","blue","yellow","orange","red"]
remove=["yellow","red"]
print(colors)
colors.remove("yellow")
print("updated color")
#take two user input two time which color to remove
#and remove them