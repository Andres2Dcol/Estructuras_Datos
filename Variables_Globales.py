a = "Barcelona"

def barca():
    
    print("Hoy juega el "+ a)
barca()

# definimos a "a " como una variable global que se va a utilizar para todas las funciones que la llamen


x = "Cali"

def cali():
    x = "Nacional"
    print("Hoy juega "+x)
cali()

print("Hoy juega el " + x)
# si se nombra una varialble x de la funcion "cali" va a ser local 
# y si se llama a imprimir esa funcion fuera de esa funcion va a ser global

#Definicion de Variable  Global

r = "Cali"

def cali():
    
    global r #definimos a r como global dentro de la funcion
    r = "Nacional"
cali()

print("Hoy juega el "+ r )