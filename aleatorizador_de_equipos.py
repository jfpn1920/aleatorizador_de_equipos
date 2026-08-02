import random
ids = []
nombres = []
categorias = []
capitanes = []
integrantes = []
ciudades = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_aleatorizador_de_equipos|--#
#---------------------------------------------#
while True:
    print("menu principal aleatorizador de equipos")
    print("1) crear equipo")
    print("2) editar equipo")
    print("3) eliminar equipo")
    print("4) buscar equipo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------#
    #--|crear_equipo|--#
    #------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_equipo = 1
        else:
            id_equipo = ids[-1] + 1
        nombre = input("nombre del equipo: ")
        categoria = input("categoría: ")
        capitan = input("capitán: ")
        cantidad = int(input("cantidad de integrantes: "))
        ciudad = input("ciudad: ")
        observacion = input("observación: ")
        ids.append(id_equipo)
        nombres.append(nombre)
        categorias.append(categoria)
        capitanes.append(capitan)
        integrantes.append(cantidad)
        ciudades.append(ciudad)
        observaciones.append(observacion)
        print("equipo registrado correctamente.")
        print("id:", id_equipo)
    #-------------------#
    #--|editar_equipo|--#
    #-------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar equipo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {capitanes[i]} | {integrantes[i]} | {ciudades[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {capitanes[posicion]} | {integrantes[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del equipo: ")
                categorias[posicion] = input("nueva categoría: ")
                capitanes[posicion] = input("nuevo capitán: ")
                integrantes[posicion] = int(input("nueva cantidad de integrantes: "))
                ciudades[posicion] = input("nueva ciudad: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|eliminar_equipo|--#
    #---------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar equipo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {capitanes[i]} | {integrantes[i]} | {ciudades[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {capitanes[posicion]} | {integrantes[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    capitanes.pop(posicion)
                    integrantes.pop(posicion)
                    ciudades.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|buscar_equipo|--#
    #-------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar equipo")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {capitanes[posicion]} | {integrantes[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            total_integrantes = 0
            mayor = integrantes[0]
            menor = integrantes[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {capitanes[i]} | {integrantes[i]} | {ciudades[i]} | {observaciones[i]}")
                total_integrantes += integrantes[i]
                if integrantes[i] > mayor:
                    mayor = integrantes[i]
                if integrantes[i] < menor:
                    menor = integrantes[i]
            promedio = total_integrantes / len(ids)
            print("estadísticas aleatorizador de equipos")
            print("cantidad de equipos:", len(ids))
            print("total de integrantes:", total_integrantes)
            print("promedio de integrantes:", round(promedio, 2))
            print("mayor cantidad de integrantes:", mayor)
            print("menor cantidad de integrantes:", menor)
            posicion = random.randint(0, len(ids) - 1)
            print("equipo seleccionado aleatoriamente")
            print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {capitanes[posicion]} | {integrantes[posicion]} | {ciudades[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de equipos.")
        break
    else:
        print("opción no válida.")