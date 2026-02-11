# Curso Python. Interfaces gráficas XI. Vídeo 52
# WIDGET MENU

from tkinter import *

root = Tk()
root.title("Prueba menú")

# varible donde guardaremos el menú----------------------------------------------------
BarraMenu = Menu(root)
root.config(menu= BarraMenu, width= 400, height=350)

# menú archivos------------------------------------------------------------------------ 
    # añadir sub-menus
ArchivoMenu= Menu(BarraMenu, tearoff= 0)      # menú principal // dentro del constructor Menu añadir un parámetro tearoff=0
ArchivoMenu.add_command(label= "Abrir archivo") # sub menú con .add_command()
ArchivoMenu.add_command(label= "Nuevo archivo")
ArchivoMenu.add_separator() 
ArchivoMenu.add_command(label= "Guardar")
ArchivoMenu.add_command(label= "Guardar como...")
ArchivoMenu.add_separator()                  # separador dentro del menú
ArchivoMenu.add_command(label= "Cerrar")
ArchivoMenu.add_command(label= "Salir")

ArchivoEditar= Menu(BarraMenu, tearoff= 0)
ArchivoEditar.add_command(label= "Deshacer")
ArchivoEditar.add_command(label= "Rehacer")
ArchivoEditar.add_separator() 
ArchivoEditar.add_command(label= "Cortar")
ArchivoEditar.add_command(label= "Copiar")
ArchivoEditar.add_command(label= "Pegar")
ArchivoEditar.add_separator() 
ArchivoEditar.add_command(label= "Encontrar")
ArchivoEditar.add_command(label= "Reemplazar")


ArchivoHerramientas= Menu(BarraMenu, tearoff= 0)


ArchivoVer= Menu(BarraMenu, tearoff= 0)
ArchivoVer.add_command(label= "Abrir visualización")
ArchivoVer.add_separator()
ArchivoVer.add_command(label= "Apariencia")
ArchivoVer.add_command(label= "Editor Layout")
ArchivoVer.add_separator()
ArchivoVer.add_command(label= "Explorar")
ArchivoVer.add_command(label= "Buscar")
ArchivoVer.add_command(label= "Probar")


ArchivoAyuda= Menu(BarraMenu, tearoff= 0)
ArchivoAyuda.add_command(label= "Licencia")
ArchivoAyuda.add_command(label= "Acerca de...")
ArchivoAyuda.add_command(label= "Documentación")
ArchivoAyuda.add_separator()
ArchivoAyuda.add_command(label= "Reportar un problema")


# para añadir texo a la opción de menú------------------------------------------------
BarraMenu.add_cascade(label= "Archivo", menu= ArchivoMenu) # añadir texto usando add_cascade(), con los parámetros Label y Menu
BarraMenu.add_cascade(label= "Editar", menu= ArchivoEditar)
BarraMenu.add_cascade(label= "Herramientas", menu= ArchivoHerramientas)
BarraMenu.add_cascade(label= "Ver", menu= ArchivoVer)
BarraMenu.add_cascade(label= "Ayuda", menu= ArchivoAyuda)




root.mainloop()