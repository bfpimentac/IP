numero= int(input())
dicataque= {}
dicdefesa= {}
listaataque=[]
listadefesa= []
for i in range(numero):
    entrada= input().split()
    aux=entrada[0:-2]
    string=" ".join(aux)
    listaataque.append(entrada[-2])
    listadefesa.append(entrada[-1])
    dicataque.update({entrada[-2]:string})
    dicdefesa.update({entrada[-1]:string})
listaataque= [int(x) for x in listaataque]
listadefesa= [int(x) for x in listadefesa]
maxataque= max(listaataque)
maxdefesa= max(listadefesa)
x=dicataque.get(f"{maxataque}")
print(f"Carta com maior poder de ataque: {x}")
print(f"Ataque: {maxataque}")
y=dicdefesa.get(f"{maxdefesa}")
print(f"\nCarta com maior poder de defesa: {y}")
print(f"Defesa: {maxdefesa}")