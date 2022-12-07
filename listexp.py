maList = [23, 56, 6, 0, -9, 0, 1, "test", 34.02]

print(maList)
print(maList[-1])

for i in range(len(maList)):
    print(maList[i])
    
maList.append([555, 12])
print(maList)

maList.insert(1, "c")
print(maList)
# pop avec index on 
maList.pop()
print(maList)
