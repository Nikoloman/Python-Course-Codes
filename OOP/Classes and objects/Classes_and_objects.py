#the class is like a model to create objects
class Cookie:
    chocolate = False

    def __init__(self, flavor = None, shape = None):
        self.flavor = flavor
        self.shape = shape

        if flavor is not None and shape is not None:
            print(f"A {flavor} cookie with the shape of a {shape} just baked!")
        else:
            print("Wtf bruh, there's no flavor and color")

    def put_chocolate(self):
        self.chocolate = True

    def have_chocolate(self):
        if self.chocolate == True:
            print("I'm a cookie with chocolate :D")
        else:
            print("I'm a cookie with no chocolate D:")

lil_cookie = Cookie("Vanilla", "Car") #initialize an object with the Cookie class

print(lil_cookie.have_chocolate())
lil_cookie.put_chocolate()
print(lil_cookie.have_chocolate())