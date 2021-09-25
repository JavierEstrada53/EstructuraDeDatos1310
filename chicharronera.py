'''Javier Figueroa Estrada
Estructura de datos'''
def la_chicharronera():

    a= float(input('Introduzca el valor de a : ')) # valor flotante
    if a == 0:
        print(' El valor de "a"  no puede ser 0')
        a= float(input('Vuelva a introducir el valor de a : '))
        b= float(input('Introduzca el valor de b : '))
        c= float(input('introduzca el valor de c : '))
    else:

        b= float(input('Introduzca el valor de b : '))
        c= float(input('introduzca el valor de c : '))
    
    #Definimos la chicharronera
    # para no llamar a otra librería, elevamos a la 0.5 = 1/2, es decir, una raíz cuadrada 
    x1 = (-b + ((b**2) - (4*a*c))**0.5 )/ (2*a)
    x2 = (-b - ((b**2) - (4*a*c))**0.5 )/ (2*a)
    resultado = f'El valor de x1 es : {x1} y el de x2 es : {x2} .'
    print(resultado)

la_chicharronera()
