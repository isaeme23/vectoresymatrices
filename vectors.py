import numpy as np

#lista
def AddVectors(a,b):
    new = []
    for i in range(len(a)):
        new.append((a[i]) + (b[i]))
    return new

#lista
def inverso(a):
    inv = []
    for i in range(len(a)):
        inv.append((-a[i]))
    return inv

#lista
def EscalarporVectorC(escalar,vector):
    mult = []
    for i in range(len(vector)):
        mult.append(int(escalar)*(vector[i]))
    return mult

#lista
def AddMatrix(matrixA, matrixB):
    matrix = []
    for i in range(len(matrixA)):
        matrix.append([])
        for j in range(len(matrixA[0])):
            matrix[i].append(matrixA[i][j] + matrixB[i][j])
    return matrix

#lista
def InvMatrix(matrix):
    inverse = []
    for i in range(len(matrix)):
        inverse.append([])
        for j in range(len(matrix[i])):
            inverse[i].append(-matrix[i][j])
    return inverse

#lista
def EscalarPorMatrixC(escalar, matrix):
    new = []
    for i in range(len(matrix)):
        new.append([])
        for j in range(len(matrix[i])):
            new[i].append(escalar*matrix[i][j])
    return new

#lista
def Transpuesta(matrix):
    transpuesta = []
    for i in range(len(matrix[0])):
        transpuesta.append([])
        for j in range(len(matrix)):
            transpuesta[i].append(matrix[j][i])
    return transpuesta

def Conjugada(matrix):
    conjugada = []
    for i in range(len(matrix)):
        conjugada.append([])
        for j in range(len(matrix[0])):
            if matrix[i][j] == complex:
                for k in range(len(matrix[i][j])):
                    if matrix[i][j][k] == "+":
                        matrix[i][j][k] = "-"
                    else:
                        matrix[i][j][k] = "+"
            conjugada[i].append(matrix[i][j])
    return conjugada

#lista
def Adjunta(matrix):
    a = []
    new = Transpuesta(matrix)
    for i in range(len(new)):
        a.append([])
        for j in range(len(new[i])):
            a[i].append(-new[i][j])
    return a

#lista
def multiplicar(matriz1, matriz2):
    resp = []
    for i in range(len(matriz1)):
        resp.append([])
        for j in range(len(matriz2[0])):
            resp[i].append(0)
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz1[0])):
                resp[i][j] += matriz1[i][k] * matriz2[k][j]
    return resp

def producto_interno(vector1, vector2):
    v = 0
    for i in range(len(vector1)):
        v += vector1[i] * vector2[i]
    return v

def norma(vec):
    n = producto_interno(vec,vec)
    return (n)*1/2

def distancia(vec1,vec2):
    one = []
    for i in range(len(vec1)):
        one.append(vec1[i]-vec2[i])
    d = norma(one)
    return d

def producto_tensor(A,B):
    tensor = np.array([[0 for i in range(len(A[0])*len(B[0]))]for j in range(len(A)*len(B))])
    for j in range(len(tensor)):
        for k in range(len(tensor)):
            tensor[j][k] = (A[j // len(B)][k // len(B[0])]) * (B[j % len(B)][k % len(B[0])])
    return tensor

def unitaria(matrix):
    one = multiplicar(matrix,Adjunta(matrix))
    two = multiplicar(Adjunta(matrix),matrix)
    if one == np.identity(len(matrix[0])) and two == np.identity(len(matrix[0])):
        return True
    else:
        return False

def hermitiana(matrix):
    if Adjunta(matrix) == matrix:
        return True
    else:
        return False