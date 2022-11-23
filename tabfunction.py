# procedure avec no return
def show(tab):
    for i in range(len(tab)):
        print("tab[%d] = %d"%(i,tab[i]))

# fonction qui re
def sigma(tab):
    somme = 0
    for i in range(len(tab)):
        somme += tab[i]
    return somme

def moy(tab):
    return sigma(tab) / len(tab)

tab1 = [12, 5, 4, 0, 67]
tab2 = [3, 5, 4, -3, 6, 90]

print("-------------------")
show(tab1)
print("la somme des elements de tab1: %d"%sigma(tab1))
print("la moyenne des elements de tab1: %d"%moy(tab1))
print("-------------------")
show(tab2)
print("la somme des elements de tab2: %d"%sigma(tab2))
print("la moyenne des elements de tab2: %d"%moy(tab2))