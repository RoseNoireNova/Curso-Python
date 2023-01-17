import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
    
    
op1=(int(input("Introduce un valor: "))) 

try:
    
    print(calculaRaiz(op1))   #Con el try se intenta que el programa imprima sin importar lo que pase y
                                            #si no puede hacerlo, se continua el flujo del código

except ValueError as ErrorDeNumeroNegativo:
    
    print(ErrorDeNumeroNegativo)

print("Programa terminado")

