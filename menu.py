#Javier Figueroa Estrada EDD 1310
#Programa para levantar orden de Menú.
#Definimos la función

def menu_select(mesa=3, comensal=2, entrada="Ensalada verde", medio="Crema de zanahoria", fuerte="Filete", adicionales="Filete término medio, la ensalada sin ningún tipo de semilla, Aderezo ranch."):
    #Establecemos los valores por default de los parámetros

    orden = f' Detalles:\n \t MESA: {int(mesa)} \n  \t COMENSAL: {int(comensal)} \n \t ENTRADA: {entrada} \n \t MEDIO: {medio}  \n \t FUERTE: {fuerte}  \n \t ADICIONALES: {adicionales} \n'
    #convertimos los string de mesa y comensal a núm enteros

    print(orden)#imprimimos la orden
    
menu_select()