TIPOS_CONSULTA = [
    "matrícula",
    "pagos",
    "constancia",
    "plataforma",
    "otro"
]

def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8

def validar_texto(texto):
    return bool(texto.strip())

# Agregamos la función de resumen aquí, tal como pediste
def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    print("\n----- RESUMEN DE SOLICITUD -----")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo de consulta: {tipo}")
    print(f"Descripción: {descripcion}")
    print(f"Prioridad: {prioridad}")
    print("--------------------------------")

def validar_tipo(tipo):
    tipo_limpio = tipo.strip().lower()
    
    if tipo_limpio in TIPOS_CONSULTA:
        return True
    else:
        return False

def calcular_prioridad(tipo):
    tipo = tipo.strip().lower()

    if tipo == "matrícula" or tipo == "plataforma":
        return "Alta"
    elif tipo == "pagos":
        return "Media"
    else:
        return "Baja"

def registrar_solicitud():
    codigo = input("Código del estudiante: ")
    
    if validar_codigo(codigo):
        print("Código válido.")
    else:
        print("Error: el código debe tener al menos 8 caracteres.")
        return 
    
    nombre = input("Nombre del estudiante: ")
    
    if validar_texto(nombre):
        print("Nombre válido.")
    else:
        print("Error: el nombre no puede estar vacío.")
        return
    
    print("Opciones de consulta: matrícula, pagos, constancia, plataforma, otro")
    tipo = input("Tipo de consulta: ")
    
    if validar_tipo(tipo):
        print("Tipo de consulta válido.")
        prioridad = calcular_prioridad(tipo)
    else:
        print("Error: tipo de consulta no válido.")
        return
        
    descripcion = input("Descripción: ")
    
    if validar_texto(descripcion):
        print("Descripción válida.")
    else:
        print("Error: la descripción no puede estar vacía.")
        return

    # Aquí modificamos el final usando la nueva función
    print("\nSolicitud registrada.")
    mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)


def menu_principal():
    while True:
        print("\n=== SOPORTE ACADÉMICO ===")
        print("1. Registrar solicitud")
        print("2. Salir")
        
        opcion = input("Elige una opción (1 o 2): ")
        
        if opcion == "1":
            registrar_solicitud()
        elif opcion == "2":
            print("Saliendo del sistema... ¡Hasta luego!")
            break  
        else:
            print("Opción no válida. Por favor, ingresa 1 o 2.")

menu_principal()