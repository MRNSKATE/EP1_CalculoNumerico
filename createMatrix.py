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
