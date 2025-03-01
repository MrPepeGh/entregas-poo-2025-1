class Producto:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def mostrar_informacion(self):
        """Mostrar la información del producto en formato de texto."""
        return f"Nombre: {self.nombre}\nPrecio unitario: ${self.precio_unitario:,.2f} COP\nCantidad: {self.cantidad} unidades\n{'-'*30}"


def solicitar_dato(mensaje, tipo_dato):
    """Solicita un dato y lo convierte al tipo especificado."""
    while True:
        try:
            dato = tipo_dato(input(mensaje))
            if tipo_dato == float and dato < 0:
                raise ValueError("El precio debe ser un valor positivo.")
            if tipo_dato == int and dato < 0:
                raise ValueError("La cantidad debe ser un valor positivo.")
            return dato
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")


def crear_producto():
    """Crea un producto pidiendo los datos al usuario."""
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = solicitar_dato("Ingrese el precio unitario en COP: ", float)
    cantidad = solicitar_dato("Ingrese la cantidad en unidades: ", int)
    
    return Producto(nombre, precio_unitario, cantidad)


def mostrar_productos(productos):
    """Muestra la información de todos los productos."""
    print("\nInformación de los productos ingresados:")
    for producto in productos:
        print(producto.mostrar_informacion())


def main():
    productos = []
    
    print("Ingrese los datos de tres productos:")

    # Pedir los datos para tres productos
    for i in range(3):
        print(f"\nProducto {i+1}:")
        producto = crear_producto()
        productos.append(producto)

    # Mostrar la información de los productos ingresados
    mostrar_productos(productos)


if __name__ == "__main__":
    main()