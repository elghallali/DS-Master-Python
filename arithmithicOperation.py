def somme(a,b):
    return a + b

def soustraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def devision(a,b):
    if(b != 0):
        return a / b
    else:
        return ""

def modulo(a,b):
    return a % b

def menu():
    
    flag = True
    while(flag == True):
        a = int(input("Entrez le numéro a: "))
        b = int(input("Entrez le numéro b: "))
        print('Merci de choiser une opération: ')
        print('1, de Opération Addistion + : ')
        print('2, de Opération Soustraction -: ')
        print('3, de Opération Multiplication * : ')
        print('4, de Opération Devision / : ')
        print('5, de Opération Modulo % : ')
        print('6, Pour quiter: ')
        case = int(input("Entrez le Opération: "))
        if case == 1:
            print("le resultat est %d"%somme(a,b))
        elif case == 2:
            print("le resultat est %d"%soustraction(a,b))
        elif case == 3:
            print("le resultat est %d"%multiplication(a,b))
        elif case == 4:
            print("le resultat est %d"%devision(a,b))
        elif case == 5:
            print("le resultat est %d"%modulo(a,b))
        elif case == 6:
            flag = False
        else:
            print("Merci de choisir un autre numéro")

menu()

