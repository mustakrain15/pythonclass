class ProductPriceError(Exception):
    pass

class Product:

    def __init__(self,name,sku,price):
        self.name=name
        self.sku=sku
        self.__price=price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price (self,price):
        if price<=0:
           # print("number cant be less then zero")
           raise ProductPriceError("price cant be less then zero")
        self.__price=price

tesirt =Product("t-shirt","123",500)
print(tesirt.__dict__)
try:
    tesirt.price= -200
except ProductPriceError as err:
    print(err)
# tesirt.price = -200
# print(f"price of t_shirt:{tesirt.price}")
print(tesirt.__dict__)




class Calculator:
    
    def __init__(self, num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2

    def differnce(self):
        return self.num1-self.num2

    def product(self):
        return self.num1*self.num2
    
    @staticmethod
    def sqtr(num):
        return num**0.5

c=Calculator(20,10)
print(c.add())
print(c.differnce())
print(c.product())
print(Calculator.sqtr(25))
