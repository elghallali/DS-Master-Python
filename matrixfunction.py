def showMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print("matrix[%d][%d]= %d"%(i,j,matrix[i][j]), end =' ')
            print(matrix[i][j], end =' ')
        print()

def transposeMatrix(matrix):
    temMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temMatrix[i][j] = matrix[j][i]
    return temMatrix


def addition(mat1, mat2):
    res = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(matrix)):
        for j in range(len(mat1[0])):
            res[i][j] = mat1[i][j] + mat2[i][j]
    return res

def soustraction(mat1, mat2):
    res = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(matrix)):
        for j in range(len(mat1[0])):
            res[i][j] = mat1[i][j] - mat2[i][j]
    return res

def multiplication(mat1, mat2):
    res = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range(len(matrix)):
        for j in range(len(mat1[0])):
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

matrix = [[2, 4, 6], [4, -6, 0], [1, 0, 1]]
matrix2 = [[1, -3, 3], [9, 6, 7], [0, -7, 1]]

print("=========================")
showMatrix((matrix))
print("=========================")
showMatrix(transposeMatrix(matrix))
print("=========================")
showMatrix(addition(matrix, matrix2))
print("=========================")
showMatrix(soustraction(matrix, matrix2))
print("=========================")
showMatrix(multiplication(matrix, matrix2))
print("=========================")