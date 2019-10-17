numero = int(input("ingrese un numero: "))

if numero % 2 == 0:
    print("el numero multiplo de 2")
elif numero % 3 == 0:
    print("el numero es multiplo de 3")
elif numero % 4 == 0:
    print("el numero multiplo de 4")
elif numero % 5 == 0:
    print("el numero es multiplo de 5")
else:
    print("el numero no es multiplo de los anteriores")
