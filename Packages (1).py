class ClassOne:
    def __init__(self):
        print("ClassOne Constructor Called")

    def method_one(self):
        print("Method of ClassOne")

class ClassTwo:
    def __init__(self):
        print("ClassTwo Constructor Called")

    def method_two(self):
        print("Method of ClassTwo")


from .classone import ClassOne
from .classtwo import ClassTwo


from mypackage import ClassOne, ClassTwo

def main():
    # Creating object of ClassOne
    obj1 = ClassOne()
    obj1.method_one()

    # Creating object of ClassTwo
    obj2 = ClassTwo()
    obj2.method_two()


# Running main function
main()
