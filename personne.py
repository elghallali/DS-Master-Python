class Person:
    def __init__(self, nom, age, genre):
        self.nom = nom
        self.age = age
        self.genre = genre
    
    def parler(self):
        return "Je suis " + self.nom + " j'ai " + str(self.age) + " ans"
    def manger(self):
        return "Je suis " + self.nom + " je mange."


p1 = Person("Mohammed", 16, "M")
p2 = Person("Maryam", 20, "F")


print(p1.parler())
print(p1.manger())

print(p2.parler())
print(p2.manger())