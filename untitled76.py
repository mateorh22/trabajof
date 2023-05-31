
import pymongo

client = pymongo.MongoClient("mongodb+srv://informatica1:bio123@cluster0.wj4huqm.mongodb.net/?retryWrites=true&w=majority")

#otro cambio

database = client["informatica1"]
equipos_collection = database["equipos"]
responsables_collection = database["responsables"]
ubicaciones_collection = database["ubicaciones"]

def validar_numero(valor):
 
 while True:

    try:
      
      return int(valor)
    
    except ValueError:
      
      print("Error: debe ingresar un numero. ")
      return None



def ingresar_equipo_manual():
  print("Ingresar nuevo equipo de forma manual ")
  serial = input("Serial: ")
  numero_activo = validar_numero(input("Numero de activo: "))
  nombre_equipo = input("Nombre del equipo: ")
  marca = input("Marca: ")
  codigo_ubicacion = validar_numero(input("Codigo de ubicacion: "))
  codigo_responsable = validar_numero(input("codigo responsable: "))

  if serial and numero_activo and nombre_equipo and marca and codigo_ubicacion and codigo_responsable:
    equipo = {
        "serial": serial,
        "numero_activo": numero_activo,
        "nombre_equipo": nombre_equipo,
        "marca":marca,
        "codigo_ubicacion": codigo_ubicacion,
        "codigo_responsable": codigo_responsable
         
    }
    equipos_collection.insert_one(equipo)
    print("Equipo ingresado extosamente")

  else:
    print("Error: faltan datos requeridos. ")



def ingresar_equipo_automatico():
    filename = input("Ingrese el nombre del archivo CSV: ")
    
    with open(filename, "r") as file:
        lines = file.read()
        
        for line in lines:
            data = line.strip().split(",")
            
            equipo = {
                "serial": data[0],
                "numero_activo": int(data[1]),
                "nombre_equipo": data[2],
                "marca": data[3],
                "codigo_ubicacion": int(data[4]),
                "codigo_responsable": int(data[5])
            }
            
            equipos_collection.insert_one(equipo)
    
    print("Equipos ingresados exitosamente.")


def actualizar_equipo():
  numero_activo = input("Ingrese el numero de activo del equipo que quiere actualizar ")

  equipo = equipos_collection.find_one({"numero_activo": int(numero_activo)})

  if equipo :
    nuevo_serial = input("Ingrese el nuevo serial: ")
    nuevo_nombre_equipo = input("Ingrese el nuevo nombre del equipo: ")
    nueva_marca = input("INgrese la nueva marca: ")
    nuevo_codigo_ubicacion = (input("Ingrese el nuevo codigo de ubicacion: "))
    nuevo_codigo_responsable = input("Ingrese el nuevo codigo de responsable: ")



    equipos_collection.update_one(
        {"numero_activo": int(numero_activo)},
        {"$set":{"serial": nuevo_serial,
                "nombre": nuevo_nombre_equipo,
                "marca": nueva_marca,
                "codigo_ubicacion": int(nuevo_codigo_ubicacion),
                "codigo_responsable": int(nuevo_codigo_responsable)}
        }
    )


    print("Equipo actualizado exitosamente. ")

  else:
    print("Equipo no encontrado")



def buscar_equipo():
  numero_activo = input("Ingrese el numero de activo dek equipo a buscar: ")
  
  equipo = equipos_collection.find_one({"numero_activo": int(numero_activo)})

  if equipo:
    print("Equipo encontrado: ")
    print(f"serial:{equipo['serial']}")
    print(f"numero de activo: {equipo['numero_activo']}")
    print(f"nombre del equipo: {equipo['nombre_equipo']}")
    print(f"marca:{equipo['marca']}")
    print(f"codigo de ubicacion: {equipo['codigo_ubicacion']}")
    print(f"codigo de responsable: {equipo['codigo_responsable']}")

  else:
    print("Equipo no encontrado.")



def ver_equipos():
  equipos = equipos_collection.find()

  print("Equipos almacenados: ")

  for equipo in equipos:
    print(f"serial: {equipo['serial']}")
    print(f"numero de activo: {equipo['numero_activo']}")
    print(f"nombre del equipo: {equipo['nombre_equipo']}")
    print(f"marca:{equipo['marca']}")
    print(f"codigo de ubicacion: {equipo['codigo_ubicacion']}")
    print(f"codigo de responsable: {equipo['codigo_responsable']}")
    print("")

def eliminar_equipo():
  numero_activo = input("Ingrese el numero de activo del equipo que quiere eliminar: ")

  equipo = equipos_collection.find_one({"numero_activo":int(numero_activo)})

  if equipo:
    equipos_collection.delete_one({"numero_activo": int(numero_activo)})
    print("Equipo eliminado exitosamente")

  else:
    print("Equipo no encontrado.")




def ingresar_responsable_manual():
    codigo_responsable = input("Ingrese el código del responsable: ")
    nombre = input("Ingrese el nombre del responsable: ")
    apellido = input("Ingrese el apellido del responsable: ")
    documento_identidad = input("Ingrese el número del documento de identidad: ")
    cargo = input("Ingrese el cargo: ")
    
    responsable = {
        "codigo_responsable": int(codigo_responsable),
        "nombre": nombre,
        "apellido": apellido,
        "documento_identidad": int(documento_identidad),
        "cargo": cargo
    }
    
    responsables_collection.insert_one(responsable)
    print("Responsable ingresado exitosamente.")


def ver_responsables():
    responsables = responsables_collection.find()
    
    print("Responsables almacenados:")
    
    for responsable in responsables:
        print(f"Código responsable: {responsable['codigo_responsable']}")
        print(f"Nombre: {responsable['nombre']}")
        print(f"Apellido: {responsable['apellido']}")
        print(f"Número de documento de identidad: {responsable['documento_identidad']}")
        print(f"Cargo: {responsable['cargo']}")
        print("")


def actualizar_responsable():

    codigo_responsable = input("Ingrese el código del responsable a actualizar: ")
    
    responsable = responsables_collection.find_one({"codigo_responsable": int(codigo_responsable)})
    
    if responsable:
        nombre = input("Ingrese el nuevo nombre del responsable: ")
        apellido = input("Ingrese el nuevo apellido del responsable: ")
        documento_identidad = input("Ingrese el nuevo número del documento de identidad: ")
        cargo = input("Ingrese el nuevo cargo: ")
        
        responsables_collection.update_one(
            {"codigo_responsable": int(codigo_responsable)},
            {
                "$set": {
                    "nombre": nombre,
                    "apellido": apellido,
                    "documento_identidad": int(documento_identidad),
                    "cargo": cargo
                }
            }
        )
        
        print("Responsable actualizado exitosamente.")
    else:
        print("Responsable no encontrado.")


def buscar_responsable():
    codigo_responsable = input("Ingrese el código del responsable a buscar: ")
    
    responsable = responsables_collection.find_one({"codigo_responsable": int(codigo_responsable)})
    
    if responsable:
        print("Responsable encontrado:")
        print(f"Código responsable: {responsable['codigo_responsable']}")
        print(f"Nombre: {responsable['nombre']}")
        print(f"Apellido: {responsable['apellido']}")
        print(f"Número de documento de identidad: {responsable['documento_identidad']}")
        print(f"Cargo: {responsable['cargo']}")
    else:
        print("Responsable no encontrado.")


def eliminar_responsable():
    codigo_responsable = input("Ingrese el código del responsable a eliminar: ")
    
    responsable = responsables_collection.find_one({"codigo_responsable": int(codigo_responsable)})
    
    if responsable:
        responsables_collection.delete_one({"codigo_responsable": int(codigo_responsable)})
        print("Responsable eliminado exitosamente.")
    else:
        print("Responsable no encontrado.")


def ingresar_ubicacion_manual():
    codigo_ubicacion = input("Ingrese el código de la ubicación: ")
    nombre = input("Ingrese el nombre de la ubicación: ")
    piso = input("Ingrese el número del piso: ")
    telefono = input("Ingrese el numero del telefono")
    
    ubicacion = {
        "codigo_ubicacion": int(codigo_ubicacion),
        "nombre": nombre,
        "piso": int(piso),
        "telefono": int(telefono)
    }
    
    ubicaciones_collection.insert_one(ubicacion)
    print("Ubicación ingresada exitosamente.")


def ver_ubicaciones():
    ubicaciones = ubicaciones_collection.find()
    
    print("Ubicaciones almacenadas:")
    
    for ubicacion in ubicaciones:
        print(f"Código de ubicación: {ubicacion['codigo_ubicacion']}")
        print(f"Nombre: {ubicacion['nombre']}")
        print(f"Piso: {ubicacion['piso']}")
        print("")

def actualizar_ubicacion():
    codigo_ubicacion = input("Ingrese el código de la ubicación a actualizar: ")
    
    ubicacion = ubicaciones_collection.find_one({"codigo_ubicacion": int(codigo_ubicacion)})
    
    if ubicacion:
        nombre = input("Ingrese el nuevo nombre de la ubicación: ")
        piso = input("Ingrese el nuevo número de piso: ")
        
        ubicaciones_collection.update_one(
            {"codigo_ubicacion": int(codigo_ubicacion)},
            {
                "$set": {
                    "nombre": nombre,
                    "piso": int(piso)
                }
            }
        )
        
        print("Ubicación actualizada exitosamente.")
    else:
        print("Ubicación no encontrada.")


def buscar_ubicacion():
    codigo_ubicacion = input("Ingrese el código de la ubicación a buscar: ")
    
    ubicacion = ubicaciones_collection.find_one({"codigo_ubicacion": int(codigo_ubicacion)})
    
    if ubicacion:
        print("Ubicación encontrada:")
        print(f"Código de ubicación: {ubicacion['codigo_ubicacion']}")
        print(f"Nombre: {ubicacion['nombre']}")
        print(f"Piso: {ubicacion['piso']}")
    else:
        print("Ubicación no encontrada.")


def eliminar_ubicacion():
    codigo_ubicacion = input("Ingrese el código de la ubicación a eliminar: ")
    
    ubicacion = ubicaciones_collection.find_one({"codigo_ubicacion": int(codigo_ubicacion)})
    
    if ubicacion:
        ubicaciones_collection.delete_one({"codigo_ubicacion": int(codigo_ubicacion)})
        print("Ubicación eliminada exitosamente.")
    else:
        print("Ubicación no encontrada.")






def menu_principal():
  while True:
    print("-------Menú principal--------")
    print("1. Gestionar informacion de equipos")
    print( "2. Gestionar infromacion de responsables")
    print("3. Gestionar infromacion de ubicacion ")
    print("4. Salir")

    opcion =  input("Seleccione una opcion \n")

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

    opcion = input("Seleccione una opcion")

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

    opcion = input("Seleccione una opcion :")

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
    print("------Menú gestion de ubcacion------")
    print("1. Ingresar una nueva ubicacion")
    print("2. Ver la la informacio de todas las ubicaciones almacenadas ")
    print("3- Actualizar la informacion de una ubicacion ")
    print("4. Eliminar una ubicacion ")
    print("5. Volveral menú principal")


    opcion = input("Seleccione una opcion ")

    if opcion == "1":
      ingresar_ubicacion_manual()

    elif opcion =="2":
      ver_ubicaciones()

    elif opcion == "3":
      actualizar_ubicacion()

    elif opcion == "4":
      eliminar_ubicacion()
    
    elif opcion == "5":
      break

    else :
      print("Error. opcion invalida seleccione otra opcion")


menu_principal()

