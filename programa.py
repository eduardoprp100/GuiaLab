def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8


def validar_texto(texto):
    return bool(texto.strip())


def validar_tipo(tipo, lista_permitida):
    return tipo.strip().lower() in lista_permitida


def calcular_prioridad(tipo):
    t = tipo.strip().lower()
    if t == "matrícula" or t == "plataforma":
        return "Alta"
    elif t == "pagos":
        return "Media"
    else:
        return "Baja"


def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    print("\n----- RESUMEN DE SOLICITUD -----")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo de consulta: {tipo}")
    print(f"Descripción: {descripcion}")
    print(f"Prioridad: {prioridad}")
    print("--------------------------------")


def registrar_solicitud():
    tipos_consulta = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    contador = 0

    while True:
        print(f"\n--- Registro {contador + 1} ---")

        codigo = input("Código del estudiante: ")
        if not validar_codigo(codigo):
            print("Error: el código debe tener al menos 8 caracteres.")
            continue

        nombre = input("Nombre del estudiante: ")
        if not validar_texto(nombre):
            print("Error: el nombre no puede estar vacío.")
            continue

        print("Opciones de consulta: matrícula, pagos, constancia, plataforma, otro")
        tipo = input("Tipo de consulta: ")
        if not validar_tipo(tipo, tipos_consulta):
            print("Error: tipo de consulta no válido.")
            continue

        descripcion = input("Descripción: ")
        if not validar_texto(descripcion):
            print("Error: la descripción no puede estar vacía.")
            continue

        prioridad = calcular_prioridad(tipo)
        contador += 1

        print(f"\n¡Solicitud {contador} registrada correctamente!")
        mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)

        # Validación para registrar mínimo 3
        if contador < 3:
            print(f"(Aviso: Debes ingresar al menos 3 solicitudes. Llevas {contador})")
        else:
            resp = input("\n¿Quieres registrar otra solicitud? (s/n): ").strip().lower()
            if resp != "s":
                print(f"\nFin del registro. Total procesadas: {contador}")
                break


def ejecutar_pruebas():
    tipos_consulta = ["matrícula", "pagos", "constancia", "plataforma", "otro"]

    print("\n--- EJECUTANDO PRUEBAS ---")

    # 1. Datos válidos
    val_cod = validar_codigo("20231005")
    val_nom = validar_texto("Juan Pérez")
    print("1. Datos válidos:", "OK" if (val_cod and val_nom) else "ERROR")

    # 2. Datos vacíos
    cod_vac = validar_codigo("")
    nom_vac = validar_texto("   ")
    print("2. Datos vacíos:", "OK" if (not cod_vac and not nom_vac) else "ERROR")

    # 3. Tipo incorrecto
    tipo_bad = validar_tipo("becas", tipos_consulta)
    print("3. Tipo incorrecto:", "OK" if not tipo_bad else "ERROR")

    # 4. Prioridad alta
    p_alta1 = calcular_prioridad("matrícula")
    p_alta2 = calcular_prioridad("plataforma")
    print("4. Prioridad Alta:", "OK" if (p_alta1 == "Alta" and p_alta2 == "Alta") else "ERROR")

    # 5. Prioridad baja
    p_baja1 = calcular_prioridad("constancia")
    p_baja2 = calcular_prioridad("otro")
    print("5. Prioridad Baja:", "OK" if (p_baja1 == "Baja" and p_baja2 == "Baja") else "ERROR")


def menu_principal():
    while True:
        print("\n=== SOPORTE ACADÉMICO ===")
        print("1. Registrar solicitud")
        print("2. Correr pruebas")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            registrar_solicitud()
        elif opcion == "2":
            ejecutar_pruebas()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()