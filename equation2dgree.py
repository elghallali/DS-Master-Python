# import the libraries
import math
print("Bonjour utilsateur: ax^2+bx+c=0")
# declaration des variables (boxe pour stocker une information!)

# initialisation des variables a, b et c :
a = float(input("Entrez le nombre a: "))
b = float(input("Entrez le nombre b: "))
c = float(input("Entrez le nombre c: "))

delta = b**2 - 4 * a * c
print("delta est: ", delta)
if delta > 0:
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)
    print("deux solutions réels x1 et x2 ")
    print("x1= ", x1)
    print("x2= ", x2 )
elif delta == 0:
    x = -b/(2*a)
    print("une seule solution est:")
    print("x= ", x)

else:
    x1= str(-b/(2*a)) + " + " + str(math.sqrt(-delta)/(2*a)) + "i"
    x2= str(-b/(2*a)) + " - " + str(math.sqrt(-delta)/(2*a)) + "i"
    print("deux solutions complexe")
    print("x1= ", x1)
    print("x2= ", x2)

