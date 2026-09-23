CATEGORIAS_SOPORTE = [
    "matrícula",
    "pagos",
    "constancia",
    "plataforma",
    "otro"
]

def verificar_categoria(categoria_ingresada):
    # Procesa el texto quitando espacios y pasándolo a minúsculas
    categoria_normalizada = categoria_ingresada.strip().lower()
    
    if categoria_normalizada in CATEGORIAS_SOPORTE:
        return True
    else:
        return False

def verificar_id(id_usuario):
    # Comprueba que no esté vacío y cumpla la longitud mínima
    return bool(id_usuario.strip()) and len(id_usuario.strip()) >= 8

def registrar_ticket():
    # 1. Solicita primero el nombre del usuario
    nombre_usuario = input("Nombre del estudiante: ")
    
    # 2. Solicita y valida el identificador/código
    id_estudiante = input("Código del estudiante: ")
    
    if verificar_id(id_estudiante):
        print("Código válido.")
    else:
        print("Código inválido. Debe tener al menos 8 caracteres.")
        return 

    # 3. Muestra las opciones y valida la categoría elegida
    print("Opciones de consulta: matrícula, pagos, constancia, plataforma, otro")
    categoria_elegida = input("Tipo de consulta: ")
    
    if verificar_categoria(categoria_elegida):
        print("Tipo válido.")
    else:
        print("Tipo de consulta inválido. Debes elegir una opción de la lista.")
        return
        
    # 4. Solicita el detalle final
    detalle_ticket = input("Descripción: ")

    # Resumen final de la solicitud
    print("\nSolicitud registrada.")
    print(f"Código: {id_estudiante}")
    print(f"Nombre: {nombre_usuario}")
    print(f"Tipo: {categoria_elegida}")
    print(f"Descripción: {detalle_ticket}")

# Ejecución de la función principal
registrar_ticket()