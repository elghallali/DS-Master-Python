# POO de class Complex 

class Complex:
    
    
    def __init__(self, reel, img):
        self.img = img
        self.reel = reel
    
    def show(self):
        if(self.img>0):
            if(self.reel==0):
                return str(abs(self.img)) + " i"
            return str(self.reel)+" + "+ str(self.img) + " i"
        elif(self.img<0):
            if(self.reel==0):
                return "- "+ str(abs(self.img)) + " i"
            return str(self.reel)+" - "+ str(abs(self.img)) + " i"
        else:
            return str(self.reel)
    
    def add(self, complex):
        return Complex(self.reel + complex.reel, self.img+ complex.img)
    
    def subtraction(self, complex):
        return Complex(self.reel - complex.reel, self.img - complex.img)
    
    def multiplication(self, complex):
        return Complex(self.reel*complex.reel - self.img*complex.img, self.reel*complex.img + self.img*complex.reel)
    
    def division(self, complex):
        reel = (self.reel*complex.reel + self.img*complex.img)/(complex.reel**2 + complex.img**2)
        img = (self.img*complex.reel - self.reel*complex.img)/(complex.reel**2 + complex.img**2)
        return Complex(reel, img)
    def __add__(self, complex):
        return Complex(self.reel + complex.reel, self.img + complex.img)

comp = Complex(1.2,-13.0)
comp1 = Complex(1.2,13.0)
comp2 = comp.add(comp1)
comp3 = comp.subtraction(comp1)
comp4 = comp.multiplication(comp1)
comp5 = comp.division(comp1)

print(comp.show())
print(comp1.show())
print(comp2.show())
print(comp3.show())
print(comp4.show())
print(comp5.show())
print("Fin du programme!")

comp6 = comp + comp1

print(comp6.show())
