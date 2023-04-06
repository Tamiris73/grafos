import numpy as np
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
        print('True')
    else:
        verticesAdjacentes = False
        print('False')
    return verticesAdjacentes
    

def tipoGrafo(matriz):
    if pseudografo(matriz)==1:
        if dirigido(matriz)==1:
            print(31)
            return 31
        else:
            print(30)
            return 30
    if multigrafo(matriz)==1:
        if dirigido(matriz)==1:
            print(21)
            return 21
        else:
            print(20)
            return 20
    if dirigido(matriz)==1:
        print(1)
        return 1
    else:
        print(0)
        return 0

def dirigido(matriz):
    l=len(matriz)    # número de linhas da matriz
    c=len(matriz[0]) # número de colunas da matriz
    for i in range (l):
        for j in range (c):
            if matriz[i][j]!=matriz[j][i]:
                return 1
    return 0
        
def multigrafo(matriz):
    l=len(matriz)    # número de linhas da matriz
    c=len(matriz[0]) # número de colunas da matriz
    for i in range (l):
        for j in range (c):
           if matriz[i][j]>1:
                return 1
    return 0
    
def pseudografo(matriz):
    l=len(matriz)    # número de linhas da matriz
    c=len(matriz[0]) # número de colunas da matriz
    for i in range (l):
        for j in range (c):
            if i==j:
                if matriz[i][j] != 0:
                    return 1
    return 0


def calcDensidade(matriz):
    tam=len(matriz)
    a=sum(sum(i) for i in matriz)
    if tipoGrafo==0:
        d=round(2*a/(tam*(tam-1)), 3)
    else: 
        d=round((a)/(tam*(tam-1)), 3)
    print(d)


def insereAresta(matriz, vi, vj):
    if matriz[vi][vj] == matriz[vj][vi]:
        matriz[vi][vj]+=1;
        matriz[vj][vi]+=1;
    else: 
        matriz[vi][vj]+=1;
    print(matriz)


def insereVertice(matriz):
    matriz = np.array(matriz)
    nl = np.zeros(len(matriz))
    matriz = np.vstack([matriz, nl])
    nc = np.zeros((len(matriz), 1))
    matriz = np.hstack([matriz, nc])
    matriz = np.array(matriz, 'int16')
    print(matriz)


def removeVertice(matriz, v):
    matriz = np.array(matriz, 'int16')
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][v] = -1
            matriz[v][j] = -1

    print(matriz)

def removeAresta(matriz, vi, vj):
    if matriz[vi][vj]==matriz[vj][vi]:
        matriz[vi][vj]=0;
        matriz[vj][vi]=0;
    else: 
        matriz[vi][vj]=0;
    print(matriz)