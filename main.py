from inventory.product import Product
from inventory.actions import add_product, view_products, update_product, delete_product
from db.database import create_table

def menu():
    print("=== Sistema de Inventario ===")
    print("1. Agregar Producto")
    print("2. Ver Productos")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")

def main():
    create_table()
    while True:
        menu()
        choice = input("Selecciona una opción: ")
        
        if choice == '1':
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            product = Product(name, quantity)
            add_product(product)
            print(f"Producto {name} agregado.")
        
        elif choice == '2':
            products = view_products()
            print("ID\tNombre\tCantidad")
            for product in products:
                print(f"{product[0]}\t{product[1]}\t{product[2]}")
        
        elif choice == '3':
            product_id = int(input("ID del producto a actualizar: "))
            new_quantity = int(input("Nueva cantidad: "))
            update_product(product_id, new_quantity)
            print(f"Producto {product_id} actualizado.")
        
        elif choice == '4':
            product_id = int(input("ID del producto a eliminar: "))
            delete_product(product_id)
            print(f"Producto {product_id} eliminado.")
        
        elif choice == '5':
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
