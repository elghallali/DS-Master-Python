class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def afficher(self):
        print(f"L'animal {self.name} , son age est {self.age}")
        print()


class Dog(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

n = Dog("Dog",2,"yellow")

print(n.age)
print(n.afficher())