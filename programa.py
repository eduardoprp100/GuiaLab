# ==========================================
# 1. FUNCIÓN PRINCIPAL (Punto de control)
# ==========================================
def menu_principal():
    """Muestra el menú interactivo al usuario."""
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


# ==========================================
# 2. GESTIÓN Y FLUJO DEL REGISTRO
# ==========================================
def registrar_solicitud():
    """Captura las entradas del usuario y coordina la validación de los datos."""
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
    # Envío de parámetros a la función de salida
    mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad)


# ==========================================
# 3. FUNCIONES AUXILIARES DE VALIDACIÓN
# ==========================================
def validar_codigo(codigo):
    """Comprueba que el código no esté vacío y contenga mínimo 8 caracteres."""
    return bool(codigo.strip()) and len(codigo.strip()) >= 8


def validar_texto(texto):
    """Comprueba que la cadena ingresada no consista solo en espacios."""
    return bool(texto.strip())


def validar_tipo(tipo, lista_permitida):
    """Verifica si la opción elegida forma parte de la lista permitida."""
    tipo_limpio = tipo.strip().lower()
    return tipo_limpio in lista_permitida


# ==========================================
# 4. LÓGICA DE NEGOCIO Y SALIDA DE DATOS
# ==========================================
def calcular_prioridad(tipo):
    """Asigna la prioridad correspondiente según la categoría de la consulta."""
    tipo_limpio = tipo.strip().lower()

    if tipo_limpio in ["matrícula", "plataforma"]:
        return "Alta"
    elif tipo_limpio == "pagos":
        return "Media"
    else:
        return "Baja"


def mostrar_resumen(codigo, nombre, tipo, descripcion, prioridad):
    """Muestra en pantalla la consolidación de la información capturada."""
    print("\n----- RESUMEN DE SOLICITUD -----")
    print(f"Código: {codigo}")
    print(f"Nombre: {nombre}")
    print(f"Tipo de consulta: {tipo}")
    print(f"Descripción: {descripcion}")
    print(f"Prioridad: {prioridad}")
    print("--------------------------------")


# ==========================================
# INICIO DE LA EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    menu_principal()