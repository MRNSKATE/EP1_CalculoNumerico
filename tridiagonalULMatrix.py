from createMatrix import *
import numpy


def firstExercise(matrix = [[]], vectora=[], vectorb=[], vectorc=[], ordemMatrix= 0,  validation=True ):
    print('O primeiro exercício consiste em realizar uma decomposição LU de uma matriz tridiagonal.\n Lembre-se, a matriz a ser introduzida deve ser triangularizável pelo Método de Eliminação de Gauss sem trocas de linhas')

    #Verifica se a função está sendo testada ou chamada pelo usuário
    if validation == True:
        ordemMatrix, matrix, vectora, vectorb, vectorc = mapVectorFirst()

    #A Matriz U possui a seguinte consição u(i,i+1) = a(i,i+1)
    uMatrix = newSquareMatrix(ordemMatrix)
    addVectorOnMatrix("c", vectorc, uMatrix)
    uMatrix[0] = matrix[0]

    """A Matriz L é composta por uma diagonal principal formada por "1" e os multiplicadores
    Neste caso, os unicos multiplicadores não nulos são l(i+1,i). Portanto, podemos escrever os dados em um vetor"""
    lMatrix = newSquareMatrix(ordemMatrix)
    addVectorOnMatrix("b", [1]*ordemMatrix, lMatrix)
    lVector = []

    line = 1
    column = 0

    while line < ordemMatrix:
        multi = matrix[line][column]/matrix[line-1][column]
        lMatrix[line][column] = multi
        lVector.append(multi)
        for i in range(2):
            matrix[line][column] = matrix[line][column] - multi*matrix[line-1][column]
            column = column + 1
            if line == column:
                uMatrix[line][column] = vectorb[line] - multi*vectorc[line-1]
        line = line + 1
        column = line - 1

    print(f'A sua matriz U é : \n \n{numpy.array(uMatrix)} \n\n')
    print(f'O seu vetor L é: \n \n {numpy.array(lVector)},\n \n ou seja, sua matriz L é \n \n{numpy.array(lMatrix)}')

    return 