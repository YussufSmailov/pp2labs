class Shape:
    def __init__(self):
        pass
   
    def area(self):
        print("defauls area: 0")

class Square(Shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        print("area is", self.length**2)
b=Shape()
b.area()
length=int(input("vvedi dlinu"))
ar=Square(length)
ar.area()
