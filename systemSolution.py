def SystemSolution(lMatrix, uMatrix, vectorD):
    vectorY = []
    vectorY.append(vectorD[0])

    for i in range(len(lMatrix) - 1):
        yi = vectorD[i+1] - lMatrix[i+1][i]*vectorY[i]
        vectorY.append(yi)
    
    vectorX = []
    vectorX.append(vectorY[-1]/uMatrix[-1][-1]) 

    for i in range(len(uMatrix) - 1):
        xi = (vectorY[i-2] - uMatrix[i-2][i-1]*vectorX[i-1])/uMatrix[i-2][i-2]
        vectorX.insert(i-2, xi)
    
    print(vectorX)

l = [[1, 0, 0, 0], [0.25, 1, 0, 0], [0, 0.6153846153846154, 1, 0], [0, 0, -3.249999999999999, 1]]
u = [[4.0, 7.0, 0, 0, 1.0], [0, 3.25, 8.0, 0], [0, 0, -0.9230769230769234, 10.0], [0, 0, 0, 35.24999999999999]]
d = [1, 2, 3, 4]
SystemSolution(l, u, d)