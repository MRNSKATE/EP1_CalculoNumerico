def SystemSolutionUL(lMatrix, uMatrix, vectorD):
    vectorY = []
    vectorY.append(vectorD[0])

    for i in range(len(lMatrix) - 1):
        yi = vectorD[i+1] - lMatrix[i+1][i]*vectorY[i]
        vectorY.append(yi)
    
    vectorX = []
    vectorX.append(vectorY[-1]/uMatrix[-1][-1]) 

    for i in range(len(uMatrix) - 1):
        j = len(uMatrix) - 2 - i
        xi = (vectorY[j] - uMatrix[j][j+1]*vectorX[0])/uMatrix[j][j]
        vectorX.insert(0, xi)
        
    return vectorX