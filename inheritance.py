# class Person:
#     def __init__(self,name,addresss):
#         self.name=name
#         self.address=addresss

#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"address:{self.address}")

# class Student(Person):
#     def __init__(self,name,address,roll_numbeer):
#         super().__init__(name,address)
#         self.roll_number= roll_numbeer

#     def profile(self):
#          super().profile()
#          print(f"roll number :{self.roll_number}")

# class Teacher(Person):
#     def __init__(self,name,address,degination):
#             super().__init__(name,address)
#             self.degination=degination

# s=Student("hari","kathmandu",2)
# s.profile()

class user:
    def __init__(self,_id,username,pwd) :
        self._id=_id
        self.username=username
        self.pwd=pwd


class Person(user):
    def __init__(self,_id,username,pwd,name,addresss):
        super().__init__(_id,username,pwd)
        self.name=name
        self.address=addresss

    def profile(self):
        # print(f"_id:{self._id}")
        print(f"Name: {self.name}")
        print(f"address:{self.address}")
        

class Staff(Person):
    def __init__(self, _id, username, pwd, name, addresss,designation):
        super().__init__(_id, username, pwd, name, addresss)
        self.designation=designation

    def profile(self):
        print(f"id:{self._id}")
        print(f"username:{self.username}")
        super().profile()
        print(f"degination:{self.designation}")

sp=Staff("1","mustak","***","ram","kathmandu","admin")
sp.profile()
        
        

