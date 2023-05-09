fatal = False
aux1=0
aux2=0
aux3=0
morreu= False
morreu2= False
vidasj = int(input())
ataquesj = int(input())
defesasj = int(input())
fraquezasj = input()
resistenciasj= input()
if (fraquezasj != "fogo" and fraquezasj != "gelo" and fraquezasj != "eletricidade"):
    fraquezasj = "nao tem"
if (resistenciasj != "fogo" and resistenciasj != "gelo" and resistenciasj != "eletricidade"):
    resistenciasj = "nao tem"

nome = input()
vida = int(input())
ataqueen = int(input())
defesaen = int(input())
fraquezaen = input()
resistenciaen= input()
if (fraquezaen != "fogo" and fraquezaen != "gelo" and fraquezaen != "eletricidade"):
    fraquezasj = "nao tem"
if (resistenciaen != "fogo" and resistenciaen != "gelo" and resistenciaen != "eletricidade"):
    resistenciaen = "nao tem"


print("Turno: 1")
passo1= input()
if(passo1 == "Agi"):
    aux1 = "fogo"
elif(passo1 == "Bufu"):
    aux1 = "gelo"
elif(passo1== "Zio"):
    aux1 = "eletricidade"


if(aux1 == fraquezaen):
    fatal= True
    dano = int((ataquesj - defesaen) * 1.7)
    vida= vida- dano
    if  vida <=0:
        morreu= True
    print(f"Isso! São João usou {passo1} e acertou a fraqueza do adversário! A magia causou {dano} de dano em {nome} que agora tem {vida} de vida.")
elif passo1 == resistenciaen:
    dano = int((ataquesj - defesaen) * 0.5)
    vida = vida - dano
    if  vida <=0:
        morreu= True
    print(f"São João usou {passo1}, mas acertou uma resistência, portanto causou apenas"
          f" {dano} de dano em {nome} que agora tem {vida} de vida.")
else:
    dano = ataquesj- defesaen
    vida = vida - dano
    if  vida <= 0:
        morreu= True
    print(f"São João usou {passo1} e causou {dano} de dano em {nome} "
          f"que agora tem {vida} de vida.")

if morreu == True: 
    print(f"Vitória! Parece que o Nahobino São João reinará nesse solstício!")
else:
    print("Turno: 2")
    if (fatal == True): 
        print(f"{nome} teve sua fraqueza em {fraquezaen} acertada, portanto não poderá agir.")
        fatal = False
    else:
        passo2= input()
        if passo2 == "Agi":
            aux2 = "fogo"
        elif passo2 == "Bufu":
            aux2 = "gelo"
        elif passo2 == "Zio":
            aux2 = "eletricidade"

        if passo2 == fraquezasj:
            fatal = True
            dano = int((ataqueen - defesasj) * 1.7)
            vidasj = vidasj - dano
            if vidasj <= 0:
                morreu2= True
                
            print(f"Vixe! {nome} usou {passo2} e acertou sua fraqueza!"
                  f" A magia causou {dano} de dano em São João que agora tem {vidasj} de vida.")
        elif passo2 == fraquezasj:
            dano = int((ataqueen - defesasj) * 0.5)
            vidasj = vidasj - dano
            if vidasj <= 0:
                morreu2= True
            print(f"{nome} usou {passo2}, mas acertou uma resistência, portanto causou apenas"
                  f" {dano} de dano em São João que agora tem {vidasj} de vida.")
        else:
            dano = ataqueen - defesasj
            vidasj= vidasj - dano
            if vidasj <= 0:
                morreu2= True
            print(f"{nome} usou {passo2} e causou {dano} de dano em São João "
                  f"que agora tem {vidasj} de vida.")
c= 0
if morreu== False and morreu2== True:
    print(f"Morremos… Parece que {nome} tem mais chances de ascender ao trono da Midsommar…")
elif(morreu2==False and morreu==False):
    print("Turno: 3")
    if fatal == True:
        print(f"São João teve sua fraqueza em {fraquezasj} acertada, portanto não poderá agir.")
        fatal = False
    else:
        passo3 = input()
        if passo3 == "Agi":
            passo3 = "fogo"
        elif passo3 == "Bufu":
            passo3 = "gelo"
        elif passo3 == "Zio":
            passo3 = "eletricidade"

        if aux3 == fraquezaen:
            fatal = True
            dano = int((ataquesj - defesaen) * 1.7)
            vida = vida - dano
            if vida <= 0:
                morreu= True
            print(f"Isso! São João usou {passo3} e acertou a fraqueza do adversário!"
                  f" A magia causou {dano} de dano em {nome} que agora tem {vida} de vida.")
        elif passo3 == resistenciaen:
            dano = int((ataquesj - defesasj) * 0.5)
            vida = vida - dano
            if vida <= 0:
                morreu= True
            print(f"São João usou {passo3}, mas acertou uma resistência, portanto causou apenas"
                  f" {dano} de dano em {nome} que agora tem {vida} de vida.")
        else:
            dano = ataquesj - defesaen
            vida = vida - dano
            if vida <= 0:
                morreu= True
            print(f"São João usou {passo3} e causou {dano} de dano em {nome} "
                  f"que agora tem {vida} de vida.")
        
        if morreu== True:
            print("Vitória! Parece que o Nahobino São João reinará nesse solstício!")

if  morreu== False and morreu2== False:
    print("Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…")