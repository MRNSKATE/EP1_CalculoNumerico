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

def decompositionULMatrix (ordemMatrix, matrix, lMatrix, lVector, uMatrix, vectorb, vectorc):
    line = 1
    column = 0
    while line < ordemMatrix - 1:
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

    print(lMatrix)
    print(lVector)
    print(uMatrix)