#Vamos a determinar el valor de verdad de algunos valores

print(17 > 7)
print(17 == 17) # el doble igual se utliza para comparar
print(17< 7) 

a = 17
b = 5

if a > b:  
  print(a, "es mayor que ",b)
else:
  print(a, " no es mayor que ",b)  
  
#cundo se pide identificar un valor booleano y recibe informacion automaticamente se vuelve un enunciado verdadero

print(bool("Barcelona"))
print(bool(17))

#valores booleanos falsos 

print(bool(False))
print(bool())
print(bool(0))
print(bool([]))

#funciones que devuelven un valor booleano 

def booleano():
  return False

print(booleano())
  
#si una funcion devuelve un valor booleano 0 la sentencia sera falsa


#vamos a ver como funciona la condicionalodad de una sentencia if cuando recibe valores booleanos 
 
def devolver() :
  return False

if devolver():
  print("Si") # si recibe un valor positivo va a tomar que cumple con la condicion
else:
  print("No")# si recibe un valor negatvo no cumpliria la condicion del if 

numero = 200
print(isinstance(numero, int))  #vamos a valorar la instancia del objeto numero y tiene que ser un valor entero
  