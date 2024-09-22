#Vamos a Modificar los Strings


#la herramoienta .upper deja toda una cadena en Mayuscula
a = "Hoy es Domingo"
print(a.upper())

#para pasar a minuscula se utiliza el .lower
b = "Hoy es Domingo"
print(b.lower())

#Para quiar los espacios de el prinipio y final de una cadena utilizamos el .strip
c = " Hoy es Domingo "
print(c.strip()) 

#Para reemplazar un caracter dentro de una cadena de texto primero lo identificamos y luego usamos la herrmaienta .replace("","")
# en las primeras comillas colocamos la que se va a cambiar y luego con la que vamos a cambiar

d = "Hoy es Domingo"
print(d.replace("H", "J"))

# ahora vamos a dividir una cadena de texto en sucadenas
#para ello usamos la herramienta .slpit (" ") en las comillas se va a identificar el texto que va a dividir la cadena de texto
a = "Hoy es Domingo"
print(a.split("es")) # retorna las cadenas ["Hoy","Domingo"]