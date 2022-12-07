class Test:
    def __init__(self):
        print("init class")
    
    def showme(self):
        return "Je suis la class sans attribut"
    
t = Test()
print(t.showme())