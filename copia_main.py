    principal =Tk()
    principal.title("Ventana Principal")
    principal.geometry("1280x700")

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.messagebox
from tabla_hash import Tabla_Hash
import tkinter.messagebox

Manager="fer"
contra="123"

tabla_principal=Tabla_Hash()

class Mi_ventan(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=500,height=450,bg='#064663')

        self.master=master
        self.pack()
        self.ventana_principal()


    def ventana_principal(self):
        
        
        #width=500,height=450,bg='#064663'
        self.bienvenida=Label(self,text="BIENVENIDO",bg='#064663', fg="white",font = ("Lemon Juice",20)).place(x=140,y=140,width=200,height=40)
        self.label_nombre=Label(self,text="USUARIO",bg='#064663',font = ("Lemon Juice",14)).place(x=25,y=200,width=130,height=40)
        self.nombre=Entry(self,font = ("Lemon Juice",14))
        self.nombre.place(x=175,y=200,width=150,height=30)
        self.label_nombre=Label(self,text="PASSWORD",bg='#064663',font = ("Lemon Juice",14)).place(x=25,y=240,width=150,height=40)
        self.password=Entry(self,font = ("Lemon Juice",14),show="*")
        self.password.place(x=175,y=240,width=150,height=30)

        self.gramatica=Button(self,text="Iniciar Secion", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=self.Iniciar_sesion).place(x=150,y=300,width=200,height=40)
        #self.automatas=Button(self,text="Registrarse", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_pila).place(x=150,y=200,width=200,height=40)
        self.salir=Button(self,text="Salir", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.quit).place(x=150,y=350,width=200,height=40)

    def Iniciar_sesion(self):
        user_manager=self.nombre.get()
        contraseña_manager=self.password.get()
        if (user_manager==Manager) and (contraseña_manager==contra):
            self.nombre.delete(0, 'end')
            self.password.delete(0, 'end')
            self.ventana_tabla()
        else:
            tkinter.messagebox.showinfo("Datos incorrectos")
        
    def ventana_tabla(self):
        self.ventana2=Toplevel()
        self.ventana2.title("Datos Empleados")
        self.ventana2.geometry("1000x700")
        self.ventana2.config(bg='#064663')

        self.Carga=Button(self.ventana2,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=carga_archivo)
        self.Cerrar_secion=Button(self.ventana2,text="Cerrar Sesión ", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=ventana2.destroy)
        self.Carga.place(x=150,y=50,width=200,height=40)
        self.Cerrar_secion.place(x=500,y=50,width=200,height=40)

        tabla = ttk.Treeview(self.ventana2, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
        tabla.column('#0', width=0)
        tabla.column('#1', width=200)
        tabla.column('#2', width=200)
        tabla.column('#3', width=200)
        tabla.column('#4', width=200)

        tabla.heading("#1", text="No.")
        tabla.heading("#2", text="Codigo Empleado")
        tabla.heading("#3", text="Nombre")
        tabla.heading("#4", text="Puesto")
        tabla.place(x=20,y=90)

        def AgregarTabla():
            tabla.delete(*tabla.get_children())
            for clave, valor in tabla_principal.tabla.items():
                print(f"Clave: {clave}, Valor: {valor.codigo}")
                tabla.insert("", "end", values=(clave, valor.codigo, valor.nombre, valor.puesto))

        if tabla_principal.utilizacion > 0:
            AgregarTabla()


        def carga_archivo():
            try:
                self.file = filedialog.askopenfilename(title="Cargar un archivo", filetypes=[("Archivos CSV", "*.csv")])

                if self.file:
                    with open(self.file, encoding="utf-8") as file:
                        self.archivo = file.read().split("\n")

                    for numero_lineas, empleados in enumerate(self.archivo):
                        if numero_lineas == 0:
                            continue  
                        id,nombre,password,puesto = empleados 
                        tabla_principal.Insertar(id,nombre,password,puesto)

                    tkinter.messagebox.showinfo("Archivo", "Se cargó el archivo con éxito")
                    AgregarTabla()
                else:
                    print('No se ha seleccionado ningún archivo')
            except FileNotFoundError:
                print('Error: Archivo no encontrado')
            except Exception as e:
                print(f'Error: {e}')
      


    
    def ventana_pila(self):
        pila=Toplevel()
        pila.title("Gramáticas")
        pila.geometry("500x500")
        pila.config(bg='#064663')

        Carga=Button(pila,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14))
        informacion=Button(pila,text="Informacion Autómata", bg="#ECB365", fg="black", font = ("Lemon Juice",14))
        validar=Button(pila,text="Validar Cadena", bg="#0E8388", fg="white", font = ("Lemon Juice",14))
        ruta=Button(pila, text='Ruta de Validacion',bg="#ECB365", fg="black", font = ("Lemon Juice",14))
        paso_paso=Button(pila,text="Recorrido paso a paso", bg="#0E8388", fg="white", font = ("Lemon Juice",12))
        una_pasada=Button(pila,text="Validar en una pasada", bg="#ECB365", fg="black", font = ("Lemon Juice",12))
        boton_salir=Button(pila, text='Salir',bg="#0E8388", fg="white", font = ("Lemon Juice",14))

        Carga.place(x=150,y=50,width=200,height=40)
        informacion.place(x=150,y=100,width=200,height=40)
        validar.place(x=150,y=150,width=200,height=40)
        ruta.place(x=150,y=200,width=200,height=40)
        paso_paso.place(x=150,y=250,width=200,height=40)
        una_pasada.place(x=150,y=300,width=200,height=40)
        boton_salir.place(x=150,y=350,width=200,height=40)

root=Tk()
app=Mi_ventan(root)
app.mainloop()
