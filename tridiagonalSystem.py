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
    
    print(matrix)
    print(vectora, vectorb, vectorc)