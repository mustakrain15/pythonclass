name=input("ENTER YOUR NAME: ")
CLASS=input("ENTER YOUR CLASS: ")
rollno=input("ENTER YOUR ROLL NUMBER: ")
science=input("ENTER THE MARKS OF SCIENCE: ")
math=input("ENTER THE MARKS OF MATH: ")
english=input("ENTER THE MARKS OF ENGLISH: ")
sum=int(science)+int(math)+int(english)
print(f"{name} of grade {CLASS} marks ")
print(f"Total mark obtain: {sum}")
percentage=(sum/300)*100
print(f"Total obtain percentage: {percentage}")
if percentage>40:
    print("congrats you have pass")
else:
    print("sorry you have fail")    