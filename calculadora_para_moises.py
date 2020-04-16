#CALCILADORA DE MOISES
resultado = 0

print("   BIENVENIDO A LA CALCULADORA   ")
print()
primer_numero = int(input("Ingrese el primer numero --> "))

print()
segundo_numero = int(input("Ingrese el segundo numero --> "))

print("1. --SUMAR------------- " )
print("2. --RESTAR------------ " )
print("3. --MULTIPLICAR------- " )
print("4. --DIVIDIR----------- " )
print("5. --SALIR DEL PROGRAMA ")
print()
opcion = int(input("Digite una opcion : "))


if opcion == 1:
    resultado = primer_numero + segundo_numero
    print("La suma es: ",resultado)
elif opcion == 2:
    resultado = primer_numero - segundo_numero
    print("La resta es:  ",resultado)
elif opcion == 3:
    resultado = primer_numero * segundo_numero
    print("La multiplicacion es: ",resultado)
elif opcion == 4:
    resultado = primer_numero / segundo_numero
    print("La division es: ",resultado)
elif opcion == 5:
    exit()
else:
    print("¡¡¡EL NUMERO DIGITADO NO PERTENESE A LA OPCIONES!!!")
    


      
