class Point:
    def __init__ (self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(f"points coordinates are ({self.x}, {self.y})")
    def move(self):
        self.move_x=int(input("for how much you wanna change x: "))
        self.move_y=int(input("for how much you wanna change y: "))
        self.new_x=self.move_x+self.x
        self.new_y=self.move_y+self.y
        print(f"points new coordinates are ({self.new_x}, {self.new_y})")
    def dist(self):
        d=((self.new_x-self.x)**2 + (self.new_y-self.y)**2)
        print(f'distance is {d}')
x=int(input())
y=int(input())
tochka=Point(x, y)
tochka.show()
tochka.move()
tochka.dist()