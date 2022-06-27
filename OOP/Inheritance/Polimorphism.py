class Product:
    def __init__(self, reference, name, price, description) -> None:
        self.reference = reference
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return """\
REFERENCE:\t{}
NAME:\t\t{}
PRICE:\t\t{}
DESCRIPTION:\t{}
        """.format(self.reference, self.name, self.price, self.description)

class Ornament(Product):
    pass

class Food(Product):
    productor = ""
    distributor = ""
    
    def __str__(self) -> str:
        return """\
REFERENCE:\t{}
NAME:\t\t{}
PRICE:\t\t{}
DESCRIPTION:\t{}
PRODUCTOR:\t{}
DISTRIBUTOR:\t{}
        """.format(self.reference, self.name, self.price, self.description, self.productor, self.distributor)

class Book(Product):
    isbn = ""
    author = ""

    def __str__(self) -> str:
        return """\
REFERENCE:\t{}
NAME:\t\t{}
PRICE:\t\t{}
DESCRIPTION:\t{}
ISBN:\t\t{}
AUTHOR:\t\t{}
        """.format(self.reference, self.name, self.price, self.description, self.isbn, self.author)

def discount_price(p, discount):
    #Return a product with a discount on it's price
    p.price = p.price - (p.price / 100 * discount)
    return p

o = Ornament(1234, "Ornamental mirror", 20, "Beautiful mirror with lots of stuff")
print(o)

f = Food(5678, "Olive Oil", 5, "250 ml")
f.productor = "Oil and more Co"
f.distributor = "Distributors of Oil"
print(f)

b = Book(1357, "Harry Potter", 10, "Book of Harry Potter and the philosopher stone")
b.isbn = "0-123456-78-9"
b.author = "J. K. Rowling"
print(b)

products = [o, f]
products.append(b)

print(products)

for p in products:
    print(p, "\n")

for p in products:
    print(p.reference, p.name)

for p in products:
    if isinstance(p, Ornament):
        print(p.reference, p.name)

    elif isinstance(p, Food):
        print(p.reference, p.name, p.productor)
    
    elif isinstance(p, Book):
        print(p.reference, p.name, p.author)

o_discount = discount_price(o, 10)
print(o_discount)
print(o)