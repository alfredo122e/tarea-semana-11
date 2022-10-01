
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog

#def mostrar():
    #imagen1=Image.open(r"C:\Users\zelay\OneDrive\Documentos\progra\pil1.jpg")
    #imagen1.show()

#carga de la imagen 
def cargar():
    archivo=filedialog.askopenfilename()
    imagen2=Image.open(archivo)
    render2=ImageTk.PhotoImage(imagen2)
    label2.configure(image=render2)
    label2.image=render2
    
    #carga de los filtros
def filtro1():
    imagen2 = imagen1.filter(ImageFilter.EMBOSS)
    imagen2.show()

def filtro2():
    imagen2 = imagen1.filter(ImageFilter.SMOOTH)
    imagen2.show()

def filtro3():
    imagen2 = imagen1.filter(ImageFilter.SHARPEN)
    imagen2.show()

def filtro4():
    imagen2 = imagen1.filter(ImageFilter.EDGE_ENHANCE)
    imagen2.show()

    #definimos color tamañp y botones de la ventana
ventana=Tk()
ventana.title("Mi primera vez usando pillow: ")
ventana.geometry("500x500")
ventana.configure(bg="turquoise")
imagen1= Image.open(r"C:\Users\zelay\OneDrive\Documentos\progra\pil5.jpg")
reducir=imagen1.resize((200,200), Image.Resampling.LANCZOS)
render=ImageTk.PhotoImage(reducir)
#bn=imagen1.convert("L")
#bn.save("pil4.jpg")
#bn.show()
render=ImageTk.PhotoImage(imagen1)
label1=Label(ventana,image=render)
label2=Label(ventana, image="")
btn2=Button(ventana,text="cargar fotografia", command=cargar,font=("Verdana",10), width=15, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff")
#btn3=Button(ventana,)
#boton1=Button(ventana,text="mostrar foto", command=mostrar)
#boton1.pack()
boton1 = Button(ventana, text="Filtro 1", command=filtro1,font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" )
boton1.pack()

boton2 = Button(ventana, text="Filtro 2", command=filtro2, font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" )
boton2.pack()

boton3 = Button(ventana, text="Filtro 3", command=filtro3, font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff")
boton3.pack()

boton4 = Button(ventana, text="Filtro 4", command=filtro4, font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff")
boton4.pack()

label1.pack()
label2.pack()
btn2.pack()
ventana.mainloop()

#alfredo jose zelaya lainez 
#david isaac fernandez chicas
