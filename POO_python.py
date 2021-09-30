#Programación Orientada a Objetos
'''
La poo es un paradigma no soportado originalmente por Python, python aneja el paradigma imperativo.
Python simula la POO con declaración de clases haciendo referencia a un objeto de forma circular.
1.forma 1
class <Nombre de la clase>:
    <definicion del cuerpo de la clase>

2. forma 2:
class <Nombre de la clase>(<Super clase>)
    <definicion del cuerpo de la clase>

El constructor se define siempre con el método __init__()
La declaración de atributos se realiza por medio de el constructor.
Para hacer encapsulamiento de métodos o atributos se debe poner ' ___ ' previo a la declaración del atributo o método.
'''
class Persona:
  def __init__(self, n, e, est):
    self.__nombre = n
    self.__edad = e
    self.__estatura = est

  def to_string(self):
    return "Nombre: " + self.__nombre + " Edad: " + str(self.__edad) + " Estatura: "+ str(self.__estatura)

  def set_estatura (self, nueva_est):
    if nueva_est > 0.10 and nueva_est < 2.5:
      self.__estatura = nueva_est
    else:
      print('Error: Esa estatura no es posible')

  def get_estatura(self):
    return self.__estatura


per = Persona("Jose", 18, 1.70)
print(per.to_string())

#encapsulamiento

per.nombre = 'Pedro'#esto no se recomienda
print(per.to_string())

per.set_estatura = 3.9
print(per.to_string())

print('Estatura: ', end = " ")
# print(per.__estatura)#el guión bajo guión bajo lo hace privado
print(per.get_estatura)

class Estudiante(Persona):
  def __init__(self, nc, nombre, edad, est):
    self.__num_cta = nc
    super().__init__(nombre,edad,est)
    
  def to_String( self ):
    return super().to_string() + 'Núm. de cuenta'+ self.__num_cta
est = Estudiante ('212020202','José',18,1.7)
print(est.to_string())
