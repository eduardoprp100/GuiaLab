# 1. FUNCIONES AUXILIARES DE VALIDACIÓN
# Ámbito: Reciben cadenas locales y devuelven booleanos. No acceden al exterior.
def validar_codigo(codigo):
    return bool(codigo.strip()) and len(codigo.strip()) >= 8

def validar_texto(texto):
    return bool(texto.strip())

def validar_tipo(tipo, lista_permitida):
    tipo_limpio = tipo.strip().lower()
    return tipo_limpio in lista_permitida


# 2. LÓGICA DE NEGOCIO Y SALIDA
# Ámbito: Reciben únicamente los datos necesarios mediante sus parámetros.
def calcular_prioridad(tipo):
    tipo_limpio = tipo.strip().lower()

    if tipo_limpio in ["matrícula", "plataforma"]:
        return "Alta"
    elif tipo_limpio == "pagos":
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


# 3. GESTIÓN DEL REGISTRO
# Ámbito: Sus variables (codigo, nombre, tipo, etc.) son exclusivamente internas.
def registrar_solicitud():
    tipos_consulta = [
        "matrícula",
        "pagos",
        "constancia",
        "plataforma",
        "otro"
    ]
    
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
    if validar_tipo(tipo, tipos_consulta):
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

    print("\nSolicitud registrada.")
    # Los datos internos se envían explícitamente a través de argumentos
    mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)


# 4. CONTROL DEL MENÚ PRINCIPAL
# Ámbito: Maneja únicamente el flujo de la interfaz inicial.
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


# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    menu_principal()