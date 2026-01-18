# main.py

from inventario import (
    agregar_producto,
    listar_productos,
    editar_producto,
    eliminar_producto
)

def mostrar_menu():
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Editar producto")
    print("4. Eliminar producto")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
