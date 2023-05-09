
def separador(entrada):
    aux= ""
    listasilabas= []
    listavogais= ["a", "e", "i", "o", "u"]
    for i in entrada:
        if i in listavogais:
            aux= aux + i    #shika ko chi kuya ma
            listasilabas.append(aux) #shi ka ko chi ku ya ma
            aux= ""
        else:
            aux= aux + i
    return listasilabas

listahospital = ["shi", "chi", "ko" , "ku", "ya", "ma"]
def verificador(silaba): #shi ka ko chi ku ya ma
    return listahospital.index(silaba)
parar= True
listaaux= []
while(parar):
    palabratoda= False
    contador= 0
    entrada= input()
    listasilabas= separador(entrada)
    for i in range(listasilabas): 
        if listasilabas[i] in listahospital:
            contador+=1
            if i== 0:
                x= verificador(listasilabas[i])
                listaaux[x]= i
                anterior= listasilabas[i]
            elif i>0:
                if verificador(i)  == verificador(anterior) + 1:
                    x= verificador(listasilabas[i])
                    listaaux[x]= i
                    anterior= listasilabas[i]
                    palavratoda= True
                if not verificador(i)  == verificador(anterior) + 1:
                    x= verificador(listasilabas[i])
                    listaaux[x]= i
                    anterior= listasilabas[i]
                    palavratoda= False 
    if listaaux== listahospital:
        parar= False
    else:
        if contador== 1:
            print(f"Lembrei! A sílaba {listaaux[0]} está no nome do hospital. Obrigada, Totoro")
        if contador>1:
            if palavratoda== True :
                string="".join(listaaux)
                print(f"A palavra {string} está toda no nome do hospital. Acertou em cheio, Totoro!")
            elif palavratoda== False:
                
        if listaaux== listahospital:
            parar= False 



    


            
            