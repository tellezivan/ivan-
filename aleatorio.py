import random
numero = []

while len(numero) < 3:
    digito = random.randint(0,9)
    if digito not in numero:
        numero.append(digito)
        
print(numero)
while True:
    while True:
        intento = input("ingrese un numero")

        usuario = []
        for i in intento:
            if int(i) not in usuario:
                usuario.append(int(i))

        if len(usuario) != len(numero):
            print("intento no valido")
        else:
            break
        
    fijas = 0
    picas = 0
    for i in range(len(numero)):
        if numero[i] == usuario[i]:
            fijas += 1

    for i in range(len(numero)):
        for j in range(len(numero)):
            if numero[i] == usuario[j] and i != j:
                picas += 1        
     
    print("fijas = " + str(fijas))
    print("picas = " + str(picas))
    if fijas == 3:
        print("en hora buena")
        break
    
    
        



