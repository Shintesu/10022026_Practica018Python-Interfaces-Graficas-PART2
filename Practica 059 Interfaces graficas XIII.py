# Curso Python. Interfaces gráficas XIII. Vídeo 54
# Ventanas emergentes: Abrir archivos
# tkinter.filedialog: Common dialogs to allow the user to specify a file to open or save.
# https://python.readthedocs.io/fr/latest/library/tkinter.html?highlight=tkinter#tkinter.WRITABLE

from tkinter import *
from tkinter import filedialog # importar filedialog

root = Tk()
root.title("Programa prueba abrir archivo")
root.config(width=400, height=500)

# ventana de abrir archivo
def AbreFichero():                                                                               # definir función de abrir fichero
    fichero = filedialog.askopenfilename(title= "Abrir", initialdir="C:",                        # retorna el directorio // initialdir dir predeterminado 
                filetypes=(("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"),      # filetypes tipo de archivo
                           ("Todos los ficheros", "*.*")))                                       
    print(fichero)                                                                               # imprime el directorio

# botón 
Button (root, text= "Abrir fichero", command=(AbreFichero)).pack()

root.mainloop()