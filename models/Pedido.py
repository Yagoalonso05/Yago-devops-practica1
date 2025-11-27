# Pedido.py
# Definición de la clase Pedido que representa un pedido realizado por un cliente.

import uuid  # para generar id único
from datetime import datetime  # para la fecha del pedido
from typing import Dict, List, Tuple
from .Usuario import Cliente  # importamos la clase Cliente para type hints

class Pedido:
    """Modelo que representa un pedido: cliente, productos con cantidades, fecha e id."""
    def __init__(self, cliente: Cliente, items: List[Tuple[str, int]], productos_lookup: Dict[str, object]) -> None:
        # Genera id único
        self.id: str = str(uuid.uuid4())
        # Fecha de creación del pedido (ahora)
        self.fecha: datetime = datetime.now()
        # Cliente que realiza el pedido
        self.cliente: Cliente = cliente
        # items es lista de tuplas (producto_id, cantidad)
        self.items: List[Tuple[str, int]] = items
        # productos_lookup es un diccionario id->Producto para calcular precios
        self.productos_lookup = productos_lookup

    def total(self) -> float:
        # Calcula el importe total recorriendo los items y sumando precio*cantidad
        total = 0.0
        for prod_id, cantidad in self.items:
            producto = self.productos_lookup.get(prod_id)
            # Si no existe el producto en lookup, se considera precio 0
            if producto is None:
                continue
            total += producto.precio * cantidad
        return total

    def __str__(self) -> str:
        # Resumen legible del pedido: id, fecha, cliente y total
        fecha_str = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return f"Pedido(id={self.id}, fecha={fecha_str}, cliente='{self.cliente.nombre}', total={self.total():.2f})"
