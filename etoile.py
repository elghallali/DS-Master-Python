n = int(input("Entre le nombre des etoiles: "))

for i in range(n+1): # lignes
    for i in range(0,i,1): # colones
        print("*", end=" ")
    print("")


for i in range(n+1): # lignes
    for i in range(n): # colones
        print("*", end=" ")
    print("")