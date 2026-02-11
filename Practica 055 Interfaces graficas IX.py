# Curso Python. Interfaces gráficas IX. Vídeo 50
# Botones de radio. Radiobuttons.

from tkinter import *

root = Tk()

VarOpcion = IntVar()                         # creamos una variable opción con valores del tipo entero
 

def imprimir():                              # definimos una función para que al pulsar una opción imprima el resultado 
    #print(VarOpcion.get())                  # imprimimos la variable opción escogida con el método .get()
    if VarOpcion.get() == 1:                 # para que imprima dentro de la ventana el resultado 
        etiqueta.config(text= "Ha escogido el género masculino")
    elif VarOpcion.get() == 2:
        etiqueta.config(text= "Ha escogido el género femenino")
    else:
        etiqueta.config(text= "Ha escogido el género Helicóptero")
Label(root, text= "Género: ").pack()         # para rescatar los valores pulsados

Radiobutton(root, text= "Masculino", variable= VarOpcion, value= 1, command= imprimir).pack()                 # asociamos una variable con nuestra variable y le asignamos un valor
Radiobutton(root, text= "Femenino", variable= VarOpcion, value= 2, command= imprimir).pack()                  # lo de arriba pero con un valor diferente // la función imprimir debe ser llamada por commnand=
Radiobutton(root, text= "Helicóptero", variable= VarOpcion, value= 3, command= imprimir).pack()               # otra opción


# añadir detalles al programa
etiqueta = Label(root)
etiqueta.pack()


root.mainloop()