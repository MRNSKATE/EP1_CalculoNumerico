from tridiagonalULMatrix import *
from createMatrix import *

def secondExercise():
    ordemMatrix = int(input("Insira a ordem da sua matriz:"))

    vectora = []
    vectorb = []
    vectorc = []
    matrix = newSquareMatrix(ordemMatrix)
    
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


    print(matrix)
    print(TMatrix)
    print(VVector)
    print(WVector)
    print(bn)