'''1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un 
método que devuelva el área del rectángulo.'''

# class Rectangulo():
#     def __init__(self, base, altura):
#         self.base=base
#         self.altura=altura

#     def area(self):
#         resultado=self.base*self.altura
#         print("El área de su rectángulo es",resultado)

# base=int(input("Ingrese la base de su rectángulo: "))
# altura=int(input("Ingrese la altura de su rectángulo: "))

# rectangulo1=Rectangulo(base,altura)
# rectangulo1.area()

'''2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
La clase debe contener como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una excepción que 
imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, 
se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad de cebadas 
restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso: “Advertencia: el mate está lavado.” 
pero no se debe lanzar una excepción.'''

# class Mate():
#     def __init__(self,maxCebadas,cantCebadas):
#         self.maxCebadas=maxCebadas
#         self.cantCebadas=cantCebadas
#         self.estado=False
        

#     def cebar(self):
#         if self.estado==False:
#             print("Se llenó el mate.")
#             self.estado=True

#         else:
#             print("¡Cuidado! ¡Te quemaste!")


#     def beber(self):
#         if self.estado==False:
#             print("¡El mate está vacío!")
#         elif self.cantCebadas<=0:
#             print("Advertencia: el mate está lavado.")
#             self.estado=False
#         else:
#             self.estado=False
#             self.cantCebadas=self.cantCebadas-1
#             print("Bebiste el mate.")

# mate1=Mate(5,3)

# mate1.cebar()
# mate1.cebar()
# mate1.beber()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()

'''3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el 
corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, 
o si el sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya un corcho.'''

# class Corcho():
#     def __init__(self,bodega):
#         self.bodega=bodega

# class Botella():
#     def __init__(self,corcho):
#         self.corcho=corcho

# class Sacacorchos():
#     def destapar(self,botella):
#         self.botella=

# '''INCOMPLETO'''

'''4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() 
guarde dos atributos: restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas 
de información, y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. 
Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que 
almacene una lista de los sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una 
instancia de la clase y llame al método.'''

# class Restaurante():
#     def __init__(self,restaurante_nombre,tipo_comida):
#         self.restaurante_nombre=restaurante_nombre
#         self.tipo_comida=tipo_comida

#     def describirRest(self):
#         print("El nombre del restaurante es",self.restaurante_nombre)
#         print("El tipo de comida que sirve es",self.tipo_comida)

#     def abrir_restaurante(self):
#         print("El restaurante está abierto.")

# class Heladeria(Restaurante):
#     def __init__(self,restaurante_nombre,tipo_comida):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores=["Limón.","Dulce de leche,","Pistacho.","Chocolate blanco."]

#     def mostrarSabores(self):
#         print("Los sabores disponibles son",self.sabores)

# restaurante1=Restaurante("Mc Donlad's.","Hamburguesas.")
# restaurante1.describirRest()
# restaurante1.abrir_restaurante()
# restaurante1=Heladeria("Mc Helados","Helados y jugos congelados.")
# restaurante1.describirRest()
# restaurante1.mostrarSabores()

'''5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos 
recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser 
menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que 
reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, 
que devuelva la cantidad cosechada'''

# class Personaje():
#     def __init__(self,vida,posicion,velocidad):
#         self.vida=vida
#         self.posicion=posicion
#         self.velocidad=velocidad

#     def recibir_ataque(self,daño):
#         self.vida=self.vida-daño
#         print("¡Has sido dañado!")
        
#         if self.vida<=0:
#             print("¡Estás muerto!")

#     def mover(self,dirección,velocidad):
#         self.dirección=dirección
#         self.velocidad=velocidad
#         print(f"Te moviste {velocidad} hacia {dirección}.")

# class Soldado(Personaje):
#     def __init__(self,vida,posicion,velocidad):
#         super().__init__(vida,posicion,velocidad)
#         self.ataque=ataque

#     def atacar(self,personaje):
#         self.personaje=personaje.recibir_ataque()

# '''INCOMPLETO'''

'''6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos 
que típicamente se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen 
de la información del usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.'''

# class Usuario():
#     def __init__(self,nombre,apellido,mail,contraseña):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.mail=mail
#         self.contraseña=contraseña

#     def describir_usuario(self):
#         print("Su mail es",self.mail,"y su contraseña es",self.contraseña)

#     def saludar_usuario(self):
#         print("Hola",self.nombre,self.apellido,"que tengas un lindo día.")

# usuario1=Usuario("María José","Gutierrez","marijo@gmail.com","1234")
# usuario2=Usuario("Tiago","Gulezzi","tiaguito@mail.com","5678")

# usuario1.describir_usuario()
# usuario2.describir_usuario()

# usuario1.saludar_usuario()
# usuario2.saludar_usuario()

'''7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede 
de la clase Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings 
tales como “puede postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() 
que muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.'''

# class Admin(Usuario):
#         def __init__(self,nombre,apellido,mail,contraseña):
#             super().__init__(nombre,apellido,mail,contraseña)
#             self.privilegios=["Puede postear en el foro.","Puede borrar un post.","Puede banear usuario.","Puede crear un grupo."]

#         def mostrar_privilegios(self):
#             print(f"Privilegios de {self.nombre} {self.apellido}:")
#             for privilegio in self.privilegios:
#                 print(privilegio)

# admin1=Admin("Francesco","Costansi","francos@gmail.com","9101")
# admin1.mostrar_privilegios()

'''8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene 
una lista de strings con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() 
de ese ejercicio a esta clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva 
instancia de Admin y use el método para mostrar privilegios.'''

# class Privilegios():
#     def __init__(self):
#         self.privilegios=["Puede postear en el foro.","Puede borrar un post.","Puede banear usuario.","Puede crear un grupo."]

#     def mostrar_privilegios(self):
#         print(f"Los privilegios del administrador son:")
#         for privilegio in self.privilegios:
#             print(privilegio)

# class Admin(Usuario):
#     def __init__(self,nombre,apellido,mail,contraseña):
#         super().__init__(nombre,apellido,mail,contraseña)
#         self.privilegios=Privilegios()

# admin2=Admin("Juan Pablo","Benavidez","jumpibenavidez@gmail.com","1213")
# admin2.describir_usuario()
# admin2.privilegios.mostrar_privilegios()

'''9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, 
e impórtela al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la 
importación funcionó.'''

# from ej9restaurante import*

# restaurante2=Restaurante("Viejo Jack II","Gourmet.")
# restaurante2.describirRest()

# '''DA ERROR'''