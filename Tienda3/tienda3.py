class Producto:
    def __init__(self, nombre, precio_unitario, cantidad, descripcion, clasificado):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificado = clasificado

    def precio_total(self):
        return self.precio_unitario * self.cantidad

    def calcula_precio(self, cantidad):
        """Devuelve el precio a pagar por la cantidad especificada."""
        return self.precio_unitario * cantidad

    def inventario_precio(self):
        """Devuelve el valor total de este producto en el inventario."""
        return self.precio_total()

    def mostrar_informacion(self):
        return f"{self.nombre:<15} | {self.cantidad:<12} | {self.precio_unitario:,.0f} COP  | {self.clasificado:<15} | {self.descripcion}"


def solicitar_dato(mensaje, tipo_dato):
    while True:
        try:
            dato = tipo_dato(input(mensaje))
            if dato > 0:
                return dato
            else:
                print("El numero debe ser positivo")
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")


def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio_unitario = solicitar_dato("Ingrese el precio unitario en COP: ", float)
    cantidad = solicitar_dato("Ingrese la cantidad en unidades: ", int)
    descripcion = input("Ingrese una descripcion al producto: ")
    clasificado = input("Ingrese la clasificación del Producto: ")

    return Producto(nombre, precio_unitario, cantidad, descripcion, clasificado)


def mostrar_productos(productos):
    print("\n{:<15} | {:<12} | {:<10} | {:<15} | {}".format("Producto", "Cantidad", "Precio", "Clasificación", "Descripción"))
    for producto in productos:
        print(producto.mostrar_informacion())


def precio_clasificacion(productos):
    resumen = {}
    for producto in productos:
        if producto.clasificado in resumen:
            resumen[producto.clasificado] += producto.precio_total()
        else:
            resumen[producto.clasificado] = producto.precio_total()

    print("\nResumen de precios por clasificación:")
    print("-" * 40)
    for clasificado, total in resumen.items():
        print(f"{clasificado:<15}: {total:,.0f} COP")


def mostrar_precios_cinco_unidades(productos):
    print("\nPrecio x5 de cada producto:")
    print("-" * 40)
    for producto in productos:
        print(f"{producto.nombre:<15}: {producto.calcula_precio(5):,.0f} COP")


def main():
    productos = []

    cantidad_productos = solicitar_dato("Cuantos productos desea ingresar?: ", int)

    for i in range(cantidad_productos):
        print(f"\nProducto {i+1}:")
        producto = crear_producto()
        productos.append(producto)

    mostrar_productos(productos)
    mostrar_precios_cinco_unidades(productos)
    precio_clasificacion(productos)


if __name__ == "__main__":
    main()