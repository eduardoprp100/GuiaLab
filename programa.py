def validar_codigo_barras(codigo):
    # Elimina espacios y verifica que sean solo números y tenga exactamente 12 dígitos
    codigo_limpio = codigo.strip()
    return codigo_limpio.isdigit() and len(codigo_limpio) == 12

def registrar_producto():
    codigo = input("Código de barras del producto (12 dígitos): ")
    
    if validar_codigo_barras(codigo):
        print("✓ Código de barras válido.")
    else:
        print("✗ Código inválido. Debe contener exactamente 12 números.")
        return  # Interrumpe el flujo si el código no es válido

    nombre_producto = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = input("Precio ($): ")

    print("\n--- Producto Registrado con Éxito ---")
    print(f"Código: {codigo.strip()}")
    print(f"Producto: {nombre_producto}")
    print(f"Categoría: {categoria}")
    print(f"Precio: ${precio}")

# Ejemplo de uso
registrar_producto()

# Cambio de prueba