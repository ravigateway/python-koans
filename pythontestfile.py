def function():
    return "pineapple"

def function2():
    return "tractor"

class Class:
    def method(self):
        return "parrot"


obj = Class()
obj.method.__self__ == obj
print(obj)