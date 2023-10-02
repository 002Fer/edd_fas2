from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.messagebox
from tabla_hash import Tabla_Hash
from tareas import Tareas
from proyectos import Proyectos
from listasimple import listaSimple
import tkinter.messagebox
import csv
import json
from arobol_avl import Arbol_AVL

Manager="fer"
contra="123"
nueva_tarea=""
nuevo_proyecto=""

tabla_principal=Tabla_Hash()
arbol=Arbol_AVL()
lista_proyectos=listaSimple()
lista_tareas=listaSimple()
def ventana_principal():
    global principal, nombre, password
    principal =Tk()
    principal.title("Ventana Principal")
    principal.geometry("500x450")
    principal.config(bg='#064663')
        
        
        #width=500,height=450,bg='#064663'
    bienvenida=Label(principal,text="BIENVENIDO",bg='#064663', fg="white",font = ("Lemon Juice",20))
    bienvenida.place(x=140,y=140,width=200,height=40)
    label_usuario=Label(principal,text="USUARIO",bg='#064663',font = ("Lemon Juice",14))
    label_usuario.place(x=25,y=200,width=130,height=40)
    nombre=Entry(principal,font = ("Lemon Juice",14))
    nombre.place(x=175,y=200,width=150,height=30)
    label_nombre=Label(principal,text="PASSWORD",bg='#064663',font = ("Lemon Juice",14))
    label_nombre.place(x=25,y=240,width=150,height=40)
    password=Entry(principal,font = ("Lemon Juice",14),show="*")
    password.place(x=175,y=240,width=150,height=30)

    gramatica=Button(principal,text="Iniciar Secion", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=Iniciar_sesion)
    gramatica.place(x=150,y=300,width=200,height=40)
        #self.automatas=Button(self,text="Registrarse", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=self.ventana_pila).place(x=150,y=200,width=200,height=40)


    principal.mainloop()

def Iniciar_sesion():
    user_manager=nombre.get()
    contraseña_manager=password.get()
    if (user_manager==Manager) and (contraseña_manager==contra):
        nombre.delete(0, 'end')
        password.delete(0, 'end')
        principal.destroy()
        ventana_tabla()
    elif tabla_principal.buscar(user_manager,contraseña_manager):
        principal.destroy()
        ventana_personal()
    else:
        tkinter.messagebox.showinfo("Datos incorrectos")
        
def ventana_tabla():
    ventana2=Tk()
    ventana2.title("Datos Empleados")
    ventana2.geometry("1000x700")
    ventana2.config(bg='#064663')

    tabla = ttk.Treeview(ventana2, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
    tabla.column('#0', width=0)
    tabla.column('#1', width=200)
    tabla.column('#2', width=200)
    tabla.column('#3', width=200)
    tabla.column('#4', width=200)

    tabla.heading("#1", text="No.")
    tabla.heading("#2", text="Codigo Empleado")
    tabla.heading("#3", text="Nombre")
    tabla.heading("#4", text="Puesto")
    
    

    def AgregarTabla():
        tabla.delete(*tabla.get_children())
        for clave, valor in tabla_principal.tabla.items():
            print(f"Clave: {clave}, Valor: {valor.codigo}")
            tabla.insert("", "end", values=(clave, valor.codigo, valor.nombre, valor.puesto))

    if tabla_principal.utilizacion > 0:
        AgregarTabla()


  
    def carga_archivo():
        file = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        if file:
            tabla.delete(*tabla.get_children()) 

            with open(file, newline="\n") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                next(lector_csv) 

                for contenido in lector_csv:
                    id,nombre,password,puesto = contenido 
                    tabla_principal.Insertar(id,nombre,password,puesto)
                tkinter.messagebox.showinfo("Se cargo el archivo")
            AgregarTabla()
    def cerrar_secion():
        ventana2.destroy()
        ventana_principal()
    
    def ventana_json():
        ventana2.destroy()
        ventana_proyectosJSON()

    

    Carga=Button(ventana2,text="Carga Archivo", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=carga_archivo)
    Cerrar_secion=Button(ventana2,text="Cerrar Sesión ", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=cerrar_secion)
    boton_json=Button(ventana2,text="Proyectos ", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=ventana_json)

    Carga.place(x=80,y=50,width=200,height=40)
    boton_json.place(x=300,y=50,width=200,height=40)
    Cerrar_secion.place(x=550,y=50,width=200,height=40)

    tabla.place(x=20,y=110)
    ventana2.mainloop()

def ventana_proyectosJSON():
    global datos
    proyectos=Tk()
    proyectos.title("ProyectUP")
    proyectos.geometry("800x700")
    proyectos.config(bg='#064663')

    tareas = ttk.Treeview(proyectos, columns=("Proyectos", "Tareas"))
    tareas.column('#0', width=0)
    tareas.column('#1', width=300)
    tareas.column('#2', width=300)

    tareas.heading("#1", text="Proyectos")
    tareas.heading("#2", text="Tareas")

    def cargar_json():
       
        file_json = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.json")])

        if file_json:
            tareas.delete(*tareas.get_children()) 
            with open(file_json, "r")as archivo_json:
                datos=json.load(archivo_json)
            
            for i in range(len(datos["Proyectos"])):
                lis_tareas=''
                id_proyectos=datos['Proyectos'][i]['id']
                nombre_proyectos=datos['Proyectos'][i]['nombre']
                nuevo_proyecto=Proyectos(id_proyectos,nombre_proyectos)
                lista_proyectos.insertar(nuevo_proyecto)

                print(id_proyectos+" ->" +nombre_proyectos)
                if len(datos['Proyectos'][i]['tareas'])>0:
                    for j in range(len(datos['Proyectos'][i]['tareas'])):
                        nombre_tareas=datos['Proyectos'][i]['tareas'][j]['nombre']
                        nombre_empleados=datos['Proyectos'][i]['tareas'][j]['empleado']
                        nueva_tarea=Tareas(nombre_tareas,nombre_empleados)
                        lista_tareas.insertar(nueva_tarea)

                        print(nombre_tareas)
                        tareas.insert("",END,text="",values=(nombre_proyectos,nombre_tareas))
            
              
                else:
                    print("\n",'|No hay tareas|')
                    tareas.insert("",END,text="",values=(nombre_proyectos,"No hay tareas"))
            
            tkinter.messagebox.showinfo("Se cargo el archivo")  

    
            for i in range(len(datos['Proyectos'])):
                arbol.Insertar(datos['Proyectos'][i]['id'])
            arbol.graficar()


    Carga=Button(proyectos,text="Cargar archivo", bg="#ECB365", fg="black", font = ("Lemon Juice",14),command=cargar_json)
    reporte=Button(proyectos,text="Reporte Proyectos", bg="#0E8388", fg="white", font = ("Lemon Juice",14))
    boton_json=Button(proyectos,text="Reporte Tareas", bg="#ECB365", fg="black", font = ("Lemon Juice",14))
    Cerrar_secion=Button(proyectos,text="Cerrar Sesión ", bg="#0E8388", fg="white", font = ("Lemon Juice",14))

    Carga.place(x=80,y=50,width=200,height=40)
    reporte.place(x=300,y=50,width=200,height=40)
    boton_json.place(x=550,y=50,width=200,height=40)
    Cerrar_secion.place(x=550,y=100,width=200,height=40)

    tareas.place(x=20,y=110)
    proyectos.mainloop()


def ventana_personal():
    global personal, nombre, password
    personal =Tk()
    personal.title("Ventana Principal")
    personal.geometry("500x450")
    personal.config(bg='#064663')
        
        
        #width=500,height=450,bg='#064663'
    bienvenida=Label(personal,text="BIENVENIDO",bg='#064663', fg="white",font = ("Lemon Juice",20))
    bienvenida.place(x=140,y=140,width=200,height=40)
    label_usuario=Label(personal,text="USUARIO",bg='#064663',font = ("Lemon Juice",14))
    label_usuario.place(x=25,y=200,width=130,height=40)
    

    gramatica=Button(personal,text="Iniciar Secion", bg="#0E8388", fg="white", font = ("Lemon Juice",14),command=Iniciar_sesion)
    gramatica.place(x=150,y=300,width=200,height=40)

    personal.mainloop()
ventana_principal()

