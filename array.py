import array as arr

a = arr.array("i",[-10, 500, 3, -7, 5])

def bubel_sort(tab):
    for i in range(len(tab)- 1):
        for j in range(len(tab) - 1):
            if(tab[j]<tab[j+1]):
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp
    return tab

print(a)
print()
print(bubel_sort(a))

"""
monTab = arr.array("i", [2, 4, 6, 8])

print("First element:", monTab[0])
print("Second element:", monTab[1])
print("Last element:", monTab[-1])


# changing first element
monTab[0] = 0
print(monTab) # Output: array('i', [0, 2, 3, 5, 7, 10])
# changing 3rd to 5th element
monTab[2:5] = arr.array('i', [4, 6, 8])
print(monTab) # Output: array('i', [0, 2, 4, 6, 8, 10])
del monTab[2] # removing third element
print(monTab) # Output: array('i', [1, 2, 3, 4])
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
b=arr.array('d',[3.7,8.6])
c=arr.array('d')
c=a+b
print("Array c = ",c)
"""