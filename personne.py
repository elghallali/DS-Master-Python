class Person:
    
    def __init__(self, nom, age, genre):
        self.nom = nom
        self.age = age
        self.genre = genre
    
    def parler(self):
        return "Je suis " + self.nom + " j'ai " + str(self.age) + " ans"
    def manger(self):
        return "Je suis " + self.nom + " je mange " + self.genre
    
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    
    def show(self):
        return "[" + self.nom + " , " + str(self.age) + " , " + self.genre + " ]"
    
class Mere:
    pass

class Student(Person):
    def __init__(self, nom, age, genre, cne):
        super().__init__(nom, age, genre)
        self.cne = cne
    def show(self):
        return "[" + self.nom + " , " + str(self.age) + " , " + self.genre + " , " + self.cne + " ]"
class Prof(Person, Mere):
    def __init__(self, nom, age, genre, numeroSomme):
        self.nom = nom
        self.age = age
        self.genre = genre
        self.numeroSomme = numeroSomme
    
    def show(self):
        return "[" + self.nom + " , " + str(self.age) + " , " + self.genre + " , " + self.numeroSomme + " ]"

p1 = Person("Mohammed", 12, "M")
print(p1.show())
p2 = Person("Maryam", 20, "F")

p1.nom = "Yassine"

print(p1.parler())
print(p1.manger())

et = Student("Yassine", 35, "M", "Z196800709")
print(et.show())

prof = Prof("Mohammed", 45, "M", "2335566")
print(prof.show())