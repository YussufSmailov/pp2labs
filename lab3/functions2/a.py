class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
   
class Smalldog(Dog):
    def __init__(self, anger):
      super().__init__(self)
      self.anger=anger
    def __str__(self):
      pass


dog=Dog("Bobik", 3)
dog=Smalldog( "angry")
print(Smalldog.age)
print(Smalldog.name)
print(Smalldog.anger)