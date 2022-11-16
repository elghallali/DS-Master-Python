a = int(input("Entrez le numéro a: "))
b = int(input("Entrez le numéro b: "))
print('Merci de choiser une opération: ')
print('1, de Opération Addistion + : ')
print('2, de Opération Soustraction -: ')
print('3, de Opération Multiplication * : ')
print('4, de Opération Devision / : ')
print('5, de Opération Modulo % : ')


case = int(input("Entrez le Opération: "))

if case == 1:
    r = a + b
    print("le resultat est %d"%r)
elif case == 2:
    r = a - b
    print("le resultat est %d"%r)
elif case == 3:
    r = a * b
    print("le resultat est %d"%r)
elif case == 4:
    r = a / b
    print("le resultat est %d"%r)
elif case == 5:
    r = a % b
    print("le resultat est %d"%r)
else:
    print("Merci de choisir un autre numéro")