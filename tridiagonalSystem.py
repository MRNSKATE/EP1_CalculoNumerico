from createMatrix import *
from systemSolution import *
import numpy

def secondExercise(matrix = [[]], vectora=[], vectorb=[], vectorc=[], vectord=[], ordemMatrix= 0,  validation=True ):
    if validation == True:
        ordemMatrix, matrix, vectora, vectorb, vectorc, vectord = mapVectorSecond()
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

    #Criação da estrutura da Matriz U
    uMatrix = newSquareMatrix(ordemMatrix - 1)
    vectorcCopy = vectorc.copy()
    del(vectorcCopy[-1])
    del(vectorcCopy[-2])
    addVectorOnMatrix("c", vectorcCopy, uMatrix)
    uMatrix[0] = matrix[0].copy()
    uMatrix[0].pop()
    TMatrixCopy = numpy.copy(TMatrix)

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

    #Encontrando o vetor y~ e o vetor z~
    
    vectordCopy = vectord.copy()
    vectordCopy.pop()
    vectory = SystemSolutionUL(lMatrix, uMatrix, vectordCopy)
    vectorz = SystemSolutionUL(lMatrix, uMatrix, VVector)

    #Encontrando xn
    xn = (vectord[-1] - (vectorc[-1]*vectory[0]) - (vectora[-1]*vectory[-2]))/(vectorb[-1] - (vectorc[-1]*vectorz[0]) - (vectora[-1]*vectorz[-2]))

    #Encontrando o x~
    for i in range(len(vectorz)):
        vectorz[i] = vectorz[i]*xn
    vectorx = subtractMatrixOneLine(vectory, vectorz)
    vectorx.append(xn)

    
    print(matrix)
    print(vectorx)
