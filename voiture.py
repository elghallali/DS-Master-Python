class Voiture:
    def __init__(self, model, marque, hp):
        self.model = model
        self.marque = marque
        self.hp = hp
    
    def demarrer(self):
        return "start " + self.marque
    
    def accelerer(self, speed):
        return self.hp * speed
    
    def stoper(self):
        print("Je me stop")