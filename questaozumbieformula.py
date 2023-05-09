frascos = int(input())
quantidadeelementos =int(input())
listaelementos= []
listanumeros =[]
soma= 0
listaelementosusados =[]
for i in range(quantidadeelementos):
    entrada= input().split(" ")
    listaelementos.append(entrada[0])
    listanumeros.append(int(entrada[1]))
for i in range(quantidadeelementos):
    sublista= listanumeros[i: ]
    for i in sublista:
        nome = listaelementos[i]
        numero = listanumeros[i]
        if numero + soma == frascos: 
            print(f"Vencemos a batalha e a humanidade foi restaurada! {listaelementosusados} foram usados para deszumbificar")
            break
        elif numero + soma<frascos: 
            soma+=numero
            listaelementosusados.append(nome)
        else:
            print("Estou sentido algo estranho... será que também vou virar zumbi?")
            break
    if soma<frascos:
        print("Estou sentido algo estranho... será que também vou virar zumbi?")