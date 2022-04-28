from tridiagonalULMatrix import *
from tridiagonalSystem import *
from createMatrix import *
import math

def createVectors(number, module):
    vectora = []
    vectorb=[]
    vectorc=[] 
    vectord = []
    for j in range(number):
        i = j + 1
        if i == number:
            ai = (2*number - 1)/(2*number)
        else:
            ai = (2*i - 1)/(4*i)
        ci = 1-ai
        vectora.append(ai)
        vectorc.append(ci)
        vectorb.append(2)
        if module == 2:
            di = math.cos((2*math.pi*(i**2))/(number**2))
            vectord.append(di)

    ordemMatrix = len(vectorb)

    if module == 1:
        matrix = newSquareMatrix(len(vectora))
        vectora.pop()
        vectorc.pop()
        addVectorOnMatrix("a", vectora, matrix)
        addVectorOnMatrix("b", vectorb, matrix)
        addVectorOnMatrix("c", vectorc, matrix)
        return  matrix, vectora, vectorb, vectorc, ordemMatrix
    if module == 2:
        matrix = newSquareMatrix(len(vectora))
        addVectorOnMatrix("a", vectora, matrix)
        addVectorOnMatrix("b", vectorb, matrix)
        addVectorOnMatrix("c", vectorc, matrix)

        return  matrix, vectora, vectorb, vectorc, vectord, ordemMatrix
            
def testAplication():
    print('Para iniciarmos os testes, escolha um módulo:')
    print('(1) Decomposição LU        (2) Resolução de sistemas')
    try:
        module = int(input('Insira o módulo: '))
    except:
        print('Ocorreu um erro inesperado, verifique os seus dados e tente novamente')


    if module != None:
        if module == 1:
            print('\n\n\n\n\n\n')
            matrix, vectora, vectorb, vectorc, ordemMatrix = createVectors(20, 1)
            print(f'A matriz de teste é: \n\n {numpy.array(matrix)} \n \n \n')
            firstExercise(matrix, vectora, vectorb, vectorc, ordemMatrix, False)
        elif module == 2:
            print('\n\n\n\n\n\n')
            matrix, vectora, vectorb, vectorc, vectord, ordemMatrix = createVectors(20, 2)
            print(f'A matriz de teste é: \n\n {numpy.array(matrix)} \n \n \n e o vetor d de teste é: \n \n{numpy.array(vectord)} \n\n\n')
            secondExercise(matrix, vectora, vectorb, vectorc, vectord, ordemMatrix, False)
        else:
            print("Escolha um módulo válido e reinicie o programa")