import numpy


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
        if len(vector) == len(matrix):
            matrix[0][len(matrix)-1] = vector[0]
            for i in range(len(vector)-1):
                matrix[i+1][i] = vector[i+1]
        else:
            for i in range(len(vector)):
                matrix[i+1][i] = vector[i]
    elif order == "b":
        for i in range(len(vector)):
            matrix[i][i] = vector[i]
    elif order == "c":
        if len(vector) == len(matrix):
            matrix[len(matrix)-1][0] = vector[len(matrix)-1]
            for i in range(len(vector)-1):
                matrix[i][i+1] = vector[i]
        else:
            for i in range(len(vector)):
                matrix[i][i+1] = vector[i]
    else:
        print("Ocorreu algum ERRO, verifique os seus dados")

def mutiplyMatrixforNumber(number, matrix):
    newMatrix = newSquareMatrix(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            item = number*matrix[i][j]
            newMatrix[i][j] = item
    return newMatrix

def subtractMatrixOneLine(firstMatrix, secondMatrix):
    newMatrix = []
    for i in range(len(firstMatrix)):
        sub = firstMatrix[i] - secondMatrix[i]
        newMatrix.append(sub)
    
    return newMatrix

def mapVectorFirst():
    correctMatrix = False
    print('O primeiro exercício consiste em realizar uma decomposição LU de uma matriz tridiagonal.\n Lembre-se, a matriz a ser introduzida deve ser triangularizável pelo Método de Eliminação de Gauss sem trocas de linhas')

    ordemMatrix = int(input("Insira a ordem da sua matriz:"))

    while correctMatrix == False:
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

        print(f'A Matriz inserida foi: \n {numpy.array(matrix)}')
        print('Para continuar o programa escolha uma das opções abaixo:')
        validate = int(input('(1) A minha matriz está correta (2) Reescrever matriz\n'))
        if validate != 2:
            correctMatrix = True

    return ordemMatrix, matrix, vectora, vectorb, vectorc

def mapVectorSecond():
    correctMatrix = False
    
    ordemMatrix = int(input("Insira a ordem da sua matriz:"))

    while correctMatrix == False:

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

        print(f'A Matriz inserida foi: \n {numpy.array(matrix)} \n \n e o vetor d foi: {numpy.array(vectord)}')
        print('Para continuar o programa escolha uma das opções abaixo:')
        validate = int(input('(1) Os meus dados estão corretos (2) Reescrever dados\n'))
        if validate != 2:
            correctMatrix = True

    return ordemMatrix, matrix, vectora, vectorb, vectorc, vectord
    