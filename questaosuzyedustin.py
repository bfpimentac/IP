quantidade = int(input())
matriz = []
maior=0
maior2= 0
listamaioresantiga= []
listalinhas= []
listacolunas= []
listadiagonal = []
maior3= 0
# vai ter quantidade linhas e quantidade colunas
for i in range(quantidade):
    listaaux= input().split(" ")
    matriz.append(listaaux) #[['2', '4', '5', '8'], ['3', '8', '5', '9'], ['1', '2', '3', '4'], ['5', '8', '9', '7']]
# somando os pares das linhas
for i in range(quantidade):
    for n in range(quantidade-1): 
          atual= int(matriz[i][n]) + int(matriz[i][n+1])
          if atual>maior:
              listalinhas = [matriz[i][n], matriz[i][n+1]]
              maior= atual

# somando os pares das colunas: 
for k in range(quantidade):
    for b in range(quantidade-1):
        atual2 = int(matriz[b][k]) + int(matriz[b+1][k])
        if atual2>maior2:
            listacolunas = [matriz[b][k], matriz[b+1][k]]
            maior2 = atual2

# verificando as diagonais agora
for x in range (quantidade-1):
        if (int(matriz[x][x])+int(matriz[x+1][x+1])) > maior3:
            maior3 = (int(matriz[x][x])+int(matriz[x+1][x+1]))
            listadiagonal= [matriz[x][x], matriz[x+1][x+1]]
stringlinhas= "".join(listalinhas)
stringcolunas= "".join(listacolunas)
stringlinhasdiagonal= "".join(listadiagonal)
senha= stringlinhas + stringcolunas + stringlinhasdiagonal
print("Falei que era fácil Dustinzinho...")
print("Pegando todas os números que formam as combinações dos pares de cada sentido temos...")
print(f"Password: {senha}")