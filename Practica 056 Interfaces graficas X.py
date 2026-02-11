# Curso Python. Interfaces gráficas X. Vídeo 51
# Check buttons


from tkinter import *

root = Tk()
root.title("Ejemplo check button")

# crear variables para añadir funcionalidad a las opciones
montagna = IntVar()
bosque = IntVar()
rio = IntVar()

# crear una función que evalúe si el check corresponde con la selección
def OpcionesViaje():

    OpcionEscogida= ""
    if(montagna.get()==1):
        OpcionEscogida+= " Montaña"
    if(bosque.get()==1):
        OpcionEscogida+= " Bosque"
    if(rio.get()==1):
        OpcionEscogida+= " Río"

    TextoFinal.config(text=OpcionEscogida)     # texto final asociado a opción escogida

# imagen mostrada
ImagenBus = PhotoImage(file= "C:/Users/Shintesu/Desktop/Python prácticas/Practica 044 Interfaces gráficas/Bus6.png") # imagen ejemplo
Label(root, image= ImagenBus).pack()

# mensaje para usuario
frame=Frame(root)                              
frame.pack() 
Label(frame, text= "Elige tus destinos", width= 75).pack()

Checkbutton(frame, text= "Montaña", variable= montagna, onvalue=1, offvalue= 0, command= OpcionesViaje).pack()     # opciones.......  // parametro  command para especificar la función a llamar cuando se pulse
Checkbutton(frame, text= "Bosque", variable= bosque, onvalue=1, offvalue= 0, command= OpcionesViaje).pack()        # ... // crear variables para asociar la variable a la opción.....
Checkbutton(frame, text= "Rio", variable= rio, onvalue=1, offvalue= 0, command= OpcionesViaje).pack()              # ... // onvalue para especificar una valor // offvalue para un valor de 0 (deselección)

# texto resultado 
TextoFinal= Label(frame)                      
TextoFinal.pack()

root.mainloop()