maList = {23, 56, 6, 0, -9, 0, 1}

print(maList)

maList.add(100)
print(maList)

maList.add(6)
print(maList)

my_set = {1, 2, 3, 4}
print(my_set)
my_set_2 = {3, 4, 5, 6}
print(my_set_2)

print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)