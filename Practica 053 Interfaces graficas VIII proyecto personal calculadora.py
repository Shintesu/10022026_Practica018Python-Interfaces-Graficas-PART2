# Curso Python. Interfaces gráficas VIII.
# CALCULADORA COMPLETA (cálculos básicos y otras caraterísticas fundamentales)
# Autor: Leisberth Andrés Cedeño Zambrano

from tkinter import * 

# ventana-------------------------------------------------------------------------------------------------
root = Tk() 
root.title("Calculadora básica")
root.config(bg="#1C1C1C")     # color de fondo

MiFrame = Frame(root, bg="#040404")
MiFrame.pack(padx=20, pady=20)  # padding

# variables globales--------------------------------------------------------------------------------------
operacion = ""      # declaramos una variable con cadena vacía
resultado = 0.0     # almacenar la suma de los valores escritos

# pantalla------------ Debe poder escribir los números presionando el clic--------------------------------

NumeroPantalla = StringVar()     

pantalla = Entry(MiFrame, textvariable = NumeroPantalla, font= ("Times New Roman", 28), bd=9, insertwidth=4, width=13,
                bg="black", fg="#2BB110", justify= "right")
pantalla.grid(row=1, column=1, padx=20, pady=20, columnspan=4)   # aumentamos el pad para el tamaño


# Crear una función para poder escribir presionando clics en pantall---PUNTO DECIMAL----------------------

def NumeroPulsado(num):     

    valor_actual = NumeroPantalla.get()
    if num == "." and "." in valor_actual:    # evitar usar más de una vez el punto/coma
        return
    NumeroPantalla.set(valor_actual+num)
    
# Definimos una función SUMA------------------------------------------------------------------------------
def suma():                                   # para almacenar debemos añadir un parámetro en la función RESTA
    global operacion, resultado               # se crea una variable global operación y resultado
    operacion = "suma"                        # almacenar dentro de la variable global operación el str suma
    try:
        resultado = float(NumeroPantalla.get())   # almacenar dentro de la variable global resultado, siendo un float
    except:
        resultado = 0
    NumeroPantalla.set("")                    # para que la calculadora vaya sumando

# Definimos una función RESTA-----------------------------------------------------------------------------
def resta():                    
    global operacion, resultado               
    operacion = "resta" 
    try:             
        resultado = float(NumeroPantalla.get())           
    except:
        resultado = 0
    NumeroPantalla.set("")   

# Definimos una función MULTIPLICACION--------------------------------------------------------------------
def multiplicacion():
    global operacion, resultado
    operacion = "multiplicacion"
    try:
        resultado = float(NumeroPantalla.get())
    except:
        resultado = 0
    NumeroPantalla.set("")

# Definimos una función DIVISIÓN------------------------------------------------------------------------
def division():
    global operacion, resultado
    operacion = "division"
    try:
        resultado = float(NumeroPantalla.get())
    except:
        resultado = 0
    NumeroPantalla.set("")

# Definir función Es_Igual (=)----------------------------------------------------------------------------
def Es_Igual():
    global resultado, operacion                      # debe operar con la variable global resultado
    try:
        segundo_num = float(NumeroPantalla.get())    # definir segundo_num

        if operacion == "suma":                                         # si la operación es igual a suma
            NumeroPantalla.set(resultado + segundo_num)    
        elif operacion == "resta":                                      # si la operación es igual a resta
            NumeroPantalla.set(resultado - segundo_num)
        elif operacion == "multiplicacion":
            NumeroPantalla.set(resultado * segundo_num)
        elif operacion == "division":
            if segundo_num != 0:
                NumeroPantalla.set(resultado / segundo_num)
            else:
                NumeroPantalla.set("ERROR")   # división por cero
        else:    
            NumeroPantalla.set("ERROR")       # luego de ejecutar el resultado la variable debe valer 0 para no generar cálculos erróneos
        resultado = 0                         # resetea el resultado
        operacion = ""                        # resetea la operación
    except:
        NumeroPantalla.set("ERROR")           # excepción
        resultado = 0                         
        operacion = ""                        

# restablecer calculadora --------------------------------------------------------------------------------
def Resetear():
    global operacion, resultado
    operacion = ""
    resultado = 0
    NumeroPantalla.set("")                    # limpiar la pantalla

# diccionario de estilo general de botones----------------------------------------------------------------
estilo_boton = {
    "width":6,
    "height":2,
    "font":("Times New Roman", 18, "bold"),
    "bg":"#000000",
    "fg":"white",
    "relief": "raised",
    "bd":4
}

# botones FILA 1 -----------------------------------------------------------------------------------------
Boton7 = Button(MiFrame, text= "7", command=lambda:NumeroPulsado("7"),**estilo_boton).grid(row= 2, column= 1, padx= 5, pady= 5)
Boton8 = Button(MiFrame, text= "8", command=lambda:NumeroPulsado("8"),**estilo_boton).grid(row= 2, column= 2, padx= 5, pady= 5)
Boton9 = Button(MiFrame, text= "9", command=lambda:NumeroPulsado("9"),**estilo_boton).grid(row= 2, column= 3, padx= 5, pady= 5)
BotonDiv = Button(MiFrame, text= "/", command=division, **estilo_boton).grid(row= 2, column= 4, padx= 5, pady= 5)

# botones FILA 2 -----------------------------------------------------------------------------------------
Boton4 = Button(MiFrame, text= "4", command=lambda:NumeroPulsado("4"),**estilo_boton).grid(row= 3, column= 1, padx= 5, pady= 5)
Boton5 = Button(MiFrame, text= "5", command=lambda:NumeroPulsado("5"),**estilo_boton).grid(row= 3, column= 2, padx= 5, pady= 5)
Boton6 = Button(MiFrame, text= "6", command=lambda:NumeroPulsado("6"),**estilo_boton).grid(row= 3, column= 3, padx= 5, pady= 5)
BotonMult = Button(MiFrame, text= "x", command=multiplicacion, **estilo_boton).grid(row= 3, column= 4, padx= 5, pady= 5)

# botones FILA 3 -----------------------------------------------------------------------------------------
Boton1 = Button(MiFrame, text= "1", command=lambda:NumeroPulsado("1"),**estilo_boton).grid(row= 4, column= 1, padx= 5, pady= 5)
Boton2 = Button(MiFrame, text= "2", command=lambda:NumeroPulsado("2"),**estilo_boton).grid(row= 4, column= 2, padx= 5, pady= 5)
Boton3 = Button(MiFrame, text= "3", command=lambda:NumeroPulsado("3"),**estilo_boton).grid(row= 4, column= 3, padx= 5, pady= 5)
BotonResta = Button(MiFrame, text= "-", command=resta, **estilo_boton).grid(row= 4, column= 4, padx= 5, pady= 5)

# botones FILA 4 -----------------------------------------------------------------------------------------
Boton0 = Button(MiFrame, text= "0", command= lambda:NumeroPulsado("0"),**estilo_boton).grid(row= 5, column= 1, padx= 5, pady= 5)
BotonPunto = Button(MiFrame, text= ".", command= lambda:NumeroPulsado("."),**estilo_boton).grid(row= 5, column= 2, padx= 5, pady= 5)
BotonSuma = Button(MiFrame, text= "+", command= suma, **estilo_boton).grid(row= 5, column= 3, padx= 5, pady= 5)
BotonIgual = Button(MiFrame, text= "=", command= Es_Igual, **estilo_boton).grid(row= 5, column= 4, padx= 5, pady= 5)

# RESET---------------------------------------------------------------------------------------------------
BotonReset = Button(MiFrame, text= "C", width= 30, height= 2, bg= "red", fg= "white", command= Resetear).grid(row= 6, column= 1, columnspan= 4, pady= 15)


# loop infinito-------------------------------------------------------------------------------------------
root.mainloop()