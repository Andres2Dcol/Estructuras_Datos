# puedes imprimir los valores string de 2 diferentes maneras

print("Hola , hoy es Domingo") #comillas
print('Hola , hoy es Domingo') #comillsa simples

#tambien puedes volver a usar cualquier tipo de comillas dentro de una cadena de texto 
print("El no  'estudio'")
print('fue dizque a "trabajar"')

#asignar valor de texto a una variable

a = "Hoy es Domingo"
print(a)

#se puede crear una cadena en mas de una linea asignandola con 3 comillas o 3 comillas simples

b = """Oh gloria inmarcesible
o jubilo inmortal , el surcos de dolores
el bien germina ya"""

print(b)


#Para imprimir el carater en una determinada poscsion podemos buscaro como un array con su respectiva poscion
#el primer caracter va tomar el valor de 0
c= "Hoy es Domingo"
print(c[1])

print()

#para imprimir linea por linea una palabra se utiliza el ciclo for simple 
for x in "platano":
  print(x)
  

#para imprimir el tamanio de una cadena de caracteres se utiliza la funcion len
d = "Hoy es Domingo"
print(len(d))

#para comprobrfa si una palabra esta dentro de una cadena de texto usamos 
e = "Hoy es Domingo"

#si la palabra "Domingo" hace parte de la cadena de texto "e" lo mandamos imprimir como un booleano verdadero
print("Domingo" in e)

#tambien lo podemos hacer verificando que una palabra NO este dentro de una cadena de texto usanto el "not in"



#ahora usando la misma logica que llevamos lo podemos hacer usando un if y mostrando que la palabra no este presente
f = "Hoy es Domingo"
if "Sabado" not in f:
  print("No, 'Sabado' No esta presente en la cadena de texto")
