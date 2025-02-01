class Shape:
    def __init__ (self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print("default area is 0")
    
class Rectangle(Shape):
    def __init__ (self, length, width):
        super().__init__(length, width)
    def area(self):
        print(f"area is {self.width*self.length}")
dlina=int(input("vvedi dlinu "))
shirina=int(input("vvedi shirinu "))
rectangle=Rectangle(dlina, shirina)
rectangle.area()
