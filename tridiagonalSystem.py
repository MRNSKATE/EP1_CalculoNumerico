from createMatrix import *
from systemSolution import *

def secondExercise():
    ordemMatrix = int(input("Insira a ordem da sua matriz:"))

    vectora = []
    vectorb = []
    vectorc = []
    matrix = newSquareMatrix(ordemMatrix)
    vectord = []

    #Mapeamento da diagonal a
    i = 0 
    while i < ordemMatrix :
        numberCell = float(input(f'Insira o valor de a{i+1}:'))
        vectora.append(numberCell)

        i = i + 1

    #Mapeamento da diagonal b
    i = 0 
    while i < ordemMatrix :
        numberCell = float(input(f'Insira o valor de b{i+1}:'))
        vectorb.append(numberCell)

        i = i + 1

    #Mapeamento da diagonal c
    i = 0 
    while i < ordemMatrix :
        numberCell = float(input(f'Insira o valor de c{i+1}:'))
        vectorc.append(numberCell)

        i = i + 1

    #Mapeamento do vetor d
    print("Muito bem, agora que você já inseriu a sua matriz A, siga os próximos passos para o mapeamento do vetor d \n")
    for i in range(len(matrix) ):
        itemd = float(input(f'Insira o item d{i+1} do seu vetor d: '))
        vectord.append(itemd)

    addVectorOnMatrix("a", vectora, matrix)
    addVectorOnMatrix("b", vectorb, matrix)
    addVectorOnMatrix("c", vectorc, matrix)

    TMatrix = []
    VVector = []
    WVector = []
    bn = matrix[-1][-1]

    #Mapeamento da Matriz T e vetor V
    for i in range(len(matrix) - 1):
        line = matrix[i].copy()
        VVector.append(line[-1])
        del(line[-1])
        TMatrix.append(line)

    #Mapeamento do vetor W
    line = matrix[len(matrix)-1].copy()
    del(line[-1])
    WVector.append(line)

    #Criação da estrutura da Matriz L
    lMatrix = newSquareMatrix(ordemMatrix - 1)
    addVectorOnMatrix("b", [1]*(ordemMatrix-1), lMatrix)
    lVector = []

    #Cração da estrutura da Matriz U
    uMatrix = newSquareMatrix(ordemMatrix - 1)
    vectorcCopy = vectorc.copy()
    del(vectorcCopy[-1])
    del(vectorcCopy[-2])
    addVectorOnMatrix("c", vectorcCopy, uMatrix)
    uMatrix[0] = matrix[0].copy()
    TMatrixCopy = TMatrix.copy()

    #Achando as Matrizes U e L da Matriz T

    line = 1
    column = 0

    while line < ordemMatrix - 1:
        multi = TMatrixCopy[line][column]/TMatrixCopy[line-1][column]
        lMatrix[line][column] = multi
        lVector.append(multi)
        for i in range(2):
            TMatrixCopy[line][column] = TMatrixCopy[line][column] - multi*TMatrixCopy[line-1][column]
            column = column + 1
            if line == column:
                uMatrix[line][column] = vectorb[line] - multi*vectorc[line-1]
        line = line + 1
        column = line - 1

    #Encontrando o vetor y~
    
    """print(matrix)
    
    print(VVector)
    print(WVector)
    print(vectord)
    print(bn)"""
    print(TMatrix)
    print(lMatrix)
    print(uMatrix)