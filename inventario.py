
inventario = []
def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("❌ Cantidad o precio inválidos.")
        return
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(producto)
    print("✅ Producto agregado correctamente.")
  
def listar_productos():
    if not inventario:
        print("📭 Inventario vacío.")
        return
      
    print("\n📦 Productos en inventario:")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}")
      
def editar_producto():
    listar_productos()
    if not inventario:
        return

    try:
        indice = int(input("Número del producto a editar: ")) - 1
        if indice < 0 or indice >= len(inventario):
            print("❌ Producto no válido.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    producto = inventario[indice]

    nuevo_nombre = input(f"Nuevo nombre ({producto['nombre']}): ").strip()
    if nuevo_nombre:
        producto["nombre"] = nuevo_nombre

    try:
        nueva_cantidad = input(f"Nueva cantidad ({producto['cantidad']}): ")
        if nueva_cantidad:
            producto["cantidad"] = int(nueva_cantidad)

        nuevo_precio = input(f"Nuevo precio ({producto['precio']}): ")
        if nuevo_precio:
            producto["precio"] = float(nuevo_precio)
    except ValueError:
        print("❌ Datos inválidos.")
        return

    print("✏️ Producto actualizado correctamente.")


def eliminar_producto():
    listar_productos()
    if not inventario:
        return

    try:
        indice = int(input("Número del producto a eliminar: ")) - 1
        if indice < 0 or indice >= len(inventario):
            print("❌ Producto no válido.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    eliminado = inventario.pop(indice)
    print(f"🗑️ Producto '{eliminado['nombre']}' eliminado.")
