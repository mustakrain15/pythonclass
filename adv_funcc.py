# 

# def welcome():
#     print("welcom back vai ")
# a=welcome
# a()


# def welcome (name):
#     print(f"welcom back vai: {name}")
# a=welcome
# a("hari")
# welcome("hehhe")

def increment(num):
    def increace_by(factor):
        return num + factor
    return increace_by
increase_by =increment(20)
print(increase_by(20))
print(increase_by(10))









def ram(number):
    def hari(factor):
        return number + factor
        return hari

    