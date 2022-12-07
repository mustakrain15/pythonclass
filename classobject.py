class Student:
   
    def __init__(self,_id,roll_no,name,gender):
        self._id = _id
        self.roll_number =roll_no
        self.name = name
        self.gender =gender
        self.total_attedence=0
    
    def veiw_attendence(self):
        return f"Total attedence of {self.name} is {self.total_attedence}"

            
s=Student(1,1,"ram","male")
#print(__dict__)
print(f"name:{s.name}")
print(f"roll number:{s.roll_number}")
s=Student(3,3,"shyam","male")
print(s.veiw_attendence())
s2= Student(2,2,"hari","female")
print(s2.veiw_attendence())

print("-"*50)


student=[]
for i in range(1,3):
    roll_n=input("enter the roll number: ")
    name =input("enter the name :")
    gender= input("enter the gender :")
    s=Student(i , roll_n, name, gender)
    student.append(s)

for student in student:
    print(f"Name:{student.name}")
    print(f"roll number:{student.roll_n}")



#repr
#str
#