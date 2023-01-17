#Estudio instrucción Raise, tiene pocas utilidades pero permite personalizar mensaje de error

def evaluaEdad(edad):
       
    if edad<0:
        raise TypeError("No se permiten edades negativas") #Se pueden crear nuestros propios errores, pero tienen que definirse antes
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate..."
  
    
print(evaluaEdad(-18))