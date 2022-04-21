
"""tridiagonalMatrix = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
matrixL = [tridiagonalMatrix[0], [0, 0, 0], [0, 0, 0]]

def findULMatrix(matrix):
    numberProcess = 1
    i = 1
    print(len(matrix))
    while numberProcess <= len(matrix) - 1:
        if (matrix[i-1][i] != 0):
            li = matrix[i][i]/matrix[i-1][i]
            print(li)
            matrixL[i][i] = li
        numberProcess += 1
        i += 1 
    """
"""for numberProcess in len(tridiagonalMatrix):
        i = 1
        if (tridiagonalMatrix[i-1][i] != 0):
            li = tridiagonalMatrix[i][i]/tridiagonalMatrix[i-1][i]
            print(li)"""

"""findULMatrix(tridiagonalMatrix)
print(matrixL)"""

#Criação da matriz quadrática de ordem N
def newSquareMatrix(ordemMatrix):
    matrix=[]
    for lines in range(ordemMatrix):
        colums = []
        for column in range(ordemMatrix):
            colums.append(0)
        matrix.append(colums)
    return matrix

def addVectorOnMatrix(order, vector, matrix):
    matrix = matrix
    if order == "a":
        for i in range(len(vector)):
            matrix[i+1][i] = vector[i]
    elif order == "b":
        for i in range(len(vector)):
            matrix[i][i] = vector[i]
    elif order == "c":
        for i in range(len(vector)):
            matrix[i][i+1] = vector[i]
    else:
        print("Ocorreu algum ERRO, verifique os seus dados")

ordemMatrix = int(input("Insira a ordem da sua matriz:"))

matrix = newSquareMatrix(ordemMatrix)
vectora = []
vectorb = []
vectorc = []

#Mapeamento da diagonal a
i = 0 
while i < ordemMatrix-1 :
    numberCell = int(input(f'Insira o valor de a{i+2}:'))
    vectora.append(numberCell)

    i = i + 1

#Mapeamento da diagonal b
i = 0 
while i < ordemMatrix :
    numberCell = int(input(f'Insira o valor de b{i}:'))
    vectorb.append(numberCell)

    i = i + 1

#Mapeamento da diagonal c
i = 0 
while i < ordemMatrix-1 :
    numberCell = int(input(f'Insira o valor de c{i+2}:'))
    vectorc.append(numberCell)

    i = i + 1

#Construção da matriz
addVectorOnMatrix("a", vectora, matrix)
addVectorOnMatrix("b", vectorb, matrix)
addVectorOnMatrix("c", vectorc, matrix)

print(matrix)

UMatrix = newSquareMatrix(ordemMatrix)
LMatrix = newSquareMatrix(ordemMatrix)
LVector = []
line = 1
column = 0

while line < ordemMatrix:
    multi = matrix[line][column]/matrix[line-1][column]
    LMatrix[line][column] = multi
    LVector.append(multi)
    for i in range(2):
        matrix[line][column] = matrix[line][column] - multi*matrix[line-1][column]
        column = column + 1
    line = line + 1
    column = line - 1

print(matrix)
print(LMatrix)
print(LVector)