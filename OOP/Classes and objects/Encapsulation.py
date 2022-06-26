class Example:
    __private_attribute = "I'm an unreachable attribute from outside"

    def __private_metod(self):
        print ("I'm an unreachable method from outside")

    def public_attribute(self):
        return self.__private_attribute

    def public_method(self):
        return self.__private_metod()

e = Example()
print(e.public_attribute())
print(e.public_method())