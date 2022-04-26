from createMatrix import *

def firstExercise():
    print('O primeiro exercício consiste em realizar uma decomposição LU de uma matriz tridiagonal.\n Lembre-se, a matriz a ser introduzida deve ser triangularizável pelo Método de Eliminação de Gauss sem trocas de linhas')
    ordemMatrix = int(input("Insira a ordem da sua matriz:"))

    matrix = newSquareMatrix(ordemMatrix)
    vectora = []
    vectorb = []
    vectorc = []

    #Mapeamento da diagonal a
    i = 0 
    while i < ordemMatrix-1 :
        numberCell = float(input(f'Insira o valor de a{i+2}:'))
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
    while i < ordemMatrix-1 :
        numberCell = float(input(f'Insira o valor de c{i+2}:'))
        vectorc.append(numberCell)

        i = i + 1

    #Construção da matriz A
    addVectorOnMatrix("a", vectora, matrix)
    addVectorOnMatrix("b", vectorb, matrix)
    addVectorOnMatrix("c", vectorc, matrix)

    #A Matriz U possui a seguinte consição u(i,i+1) = a(i,i+1)
    uMatrix = newSquareMatrix(ordemMatrix)
    addVectorOnMatrix("c", vectorc, uMatrix)
    uMatrix[0] = matrix[0]

    """A Matriz L é composta por uma diagonal principal formada por "1" e os multiplicadores
    Neste caso, os unicos multiplicadores não nulos são l(i+1,i). Portanto, podemos escrever os dados em um vetor"""
    lMatrix = newSquareMatrix(ordemMatrix)
    addVectorOnMatrix("b", [1]*ordemMatrix, lMatrix)
    lVector = []

    print(f'A Matriz introduzida foi {matrix} \n\n')

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

    print(f'A sua matriz U é : \n {uMatrix} \n\n')
    print(f'O seu vetor L é: \n {lVector},\n ou seja, sua matriz L é \n {lMatrix}')

    return 