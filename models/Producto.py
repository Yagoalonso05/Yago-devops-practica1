# Producto.py
# Definición de la clase Producto y sus subclases con comentarios por línea.

import uuid  # para generar identificadores únicos
from typing import Any  # tipo genérico para hints

class Producto:
    """Clase base que representa un producto genérico en la tienda."""
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        # Genera un id único para cada producto usando uuid4
        self.id: str = str(uuid.uuid4())  # identificador único del producto
        self.nombre: str = nombre  # nombre del producto
        self.precio: float = precio  # precio unitario del producto
        self.stock: int = stock  # unidades disponibles en inventario

    def hay_stock(self, cantidad: int) -> bool:
        # Comprueba si hay al menos 'cantidad' unidades en stock
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        # Actualiza el stock sumando (si cantidad>0) o restando (si cantidad<0)
        # Aquí no se verifica por negativo: se asume que el servicio que llama lo valida
        self.stock += cantidad

    def __str__(self) -> str:
        # Representación legible del producto (se usará en listados)
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio:.2f}, stock={self.stock})"

class ProductoElectronico(Producto):
    """Producto que añade meses de garantía."""
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> None:
        # Llamamos al constructor de la clase base
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = garantia_meses  # meses de garantía del artículo

    def __str__(self) -> str:
        # Incluye la información de garantía en la representación
        base = super().__str__()  # representación base
        return f"{base[:-1]}, garantia_meses={self.garantia_meses})"

class ProductoRopa(Producto):
    """Producto que añade talla y color."""
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        # Constructor base
        super().__init__(nombre, precio, stock)
        self.talla: str = talla  # talla de la prenda (S, M, L...)
        self.color: str = color  # color de la prenda

    def __str__(self) -> str:
        # Incluye talla y color en la representación
        base = super().__str__()
        return f"{base[:-1]}, talla='{self.talla}', color='{self.color}')"
