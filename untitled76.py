
import pymongo
import csv


# importacion de las funciones de equipo
from funciones import ingresar_equipo_manual
from funciones import ingresar_equipo_automatico
from funciones import actualizar_equipo
from funciones import buscar_equipo
from funciones import ver_equipos
from funciones import eliminar_equipo


# importacion de las funciones de responsables
from funciones import ingresar_responsable_manual
from funciones import ver_responsables
from funciones import actualizar_responsable
from funciones import eliminar_responsable
from funciones import buscar_responsable



#importacion de las funciones de ubicacion
from funciones import ingresar_ubicacion_manual
from funciones import ver_ubicaciones
from funciones import actualizar_ubicacion
from funciones import buscar_ubicacion
from funciones import eliminar_ubicacion




 
client = pymongo.MongoClient("mongodb+srv://informatica1:bio123@cluster0.wj4huqm.mongodb.net/?retryWrites=true&w=majority")


database = client["informatica1"]
equipos_collection = database["equipos"]
responsables_collection = database["responsables"]
ubicaciones_collection = database["ubicaciones"]


def validar_numero(valor):
  try:
    
    return int(valor)

  except ValueError:
    print("Error: debe ingresar solo numero ")

    return None


def menu_principal():
  while True:
    print("-------Menú principal--------")
    print("1. Gestionar informacion de equipos")
    print( "2. Gestionar infromacion de responsables")
    print("3. Gestionar infromacion de ubicacion ")
    print("4. Salir")

    opcion =  input("Seleccione una opcion:  ")

    if opcion =="1":
      menu_equipos()
    if opcion == "2":
      menu_responsables()
    if opcion == "3":
      menu_ubicaciones()
    elif opcion == "4":
      break
    else:
      print("Error: Opcion invalida Seleccione una opcion nuevamente")


def menu_equipos():
  while True:
    print("-----Menu gestion de equipos------")
    print("1. Ingresar un nuevo equipo de forma manual ")
    print("2. Ingrear un nuevo equipo de forma automatica")
    print("3. Actualizar la informacion de un equipo")
    print("4. Buscar un equipo ")
    print( "5. Ver la informacion de todos los equipos almacenados ")
    print("6. Eliminar un equipos ")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
      ingresar_equipo_manual()

    elif opcion == "2":
      ingresar_equipo_automatico()

    elif opcion == "3":
      actualizar_equipo()

    elif opcion =="4":
      buscar_equipo()

    elif opcion == "5":
      ver_equipos()

    elif opcion == "6":
      eliminar_equipo()

    elif opcion == "7":
      break

    else:
      print("Error. opcion invalida seleccione otra opcion ")

def menu_responsables():
  while True:
    print("-----Menú gstion de responsables-----")
    print("1. Ingresar un nuevo equipo ")
    print("2.Ver la informcaion de todos los responsables almacenados")
    print("3. Actualizar la informacion de un responsable")
    print("4. Eliminar un responsable")
    print("5. Volver al menu principal")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
      ingresar_responsable_manual()
      

    elif opcion == "2":
      ver_responsables()

    elif opcion =="3":
      actualizar_responsable()

    elif opcion == "4":
      eliminar_responsable()

    elif opcion == "5":
      break

    else:
      print("Error . opcion invalida seleccione otra opcion")




def menu_ubicaciones():
  while True:
    print("-----Menú gestion de ubicación-------")
    print("1. Ingrese una ubicaion ")
    print("2. Ver la informacion de todas la ubicaciones almacenadas ")
    print("3. Actualizar la informacion de una ubicacion ")
    print("4. Eliminar una ubicaion ")
    print("5. Volver al menú principal ")

    opcion = input("seleccione una opcion")

    if opcion =="1":
      ingresar_ubicacion_manual()

    elif opcion == "2":
      ver_ubicaciones()

    elif opcion =="3":
      actualizar_ubicacion()

    elif opcion == "4":
      eliminar_ubicacion

    elif opcion == "5":
      break

    else:
      print("Error. opcion invalida seleccione otra")



menu_principal()


