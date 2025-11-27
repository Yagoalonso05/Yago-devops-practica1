# Tienda_service.py
# Implementa la lógica de negocio: gestión de usuarios, productos y pedidos.

from typing import Dict, List, Tuple, Optional
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Usuario import Usuario, Cliente, Administrador
from models.Pedido import Pedido

class TiendaService:
    """Servicio que actúa como intermediario para operaciones de la tienda."""
    def __init__(self) -> None:
        # Diccionarios para almacenar objetos por su id
        self.usuarios: Dict[str, Usuario] = {}  # id -> Usuario
        self.productos: Dict[str, Producto] = {}  # id -> Producto
        self.pedidos: Dict[str, Pedido] = {}  # id -> Pedido

    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: Optional[str] = None) -> Usuario:
        # Crea y registra un usuario de tipo 'cliente' o 'admin'
        tipo = tipo.lower()
        if tipo == 'cliente':
            u = Cliente(nombre, email, direccion)
        elif tipo == 'administrador' or tipo == 'admin':
            u = Administrador(nombre, email)
        else:
            raise ValueError('Tipo de usuario no reconocido: use "cliente" o "administrador"')
        # Almacena el usuario en el diccionario y lo devuelve
        self.usuarios[u.id] = u
        return u

    def añadir_producto(self, producto: Producto) -> None:
        # Añade un producto al inventario usando su id como clave
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> bool:
        # Elimina un producto por id; devuelve True si existía y se eliminó
        if producto_id in self.productos:
            del self.productos[producto_id]
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        # Devuelve una lista de productos actualmente en el inventario
        return list(self.productos.values())

    def crear_pedido(self, usuario_id: str, items: List[Tuple[str, int]]) -> Pedido:
        """Crea un pedido si el usuario existe y hay stock suficiente.
        items: lista de (producto_id, cantidad)
        """
        # Verificar usuario
        usuario = self.usuarios.get(usuario_id)
        if usuario is None:
            raise ValueError('Usuario no encontrado')
        # Solo clientes pueden hacer pedidos (según especificación)
        if not isinstance(usuario, Cliente):
            raise ValueError('Solo clientes pueden realizar pedidos')

        # Verificar stock de todos los items antes de modificar nada
        for prod_id, cantidad in items:
            producto = self.productos.get(prod_id)
            if producto is None:
                raise ValueError(f'Producto con id {prod_id} no existe')
            if cantidad <= 0:
                raise ValueError('La cantidad debe ser mayor que 0')
            if not producto.hay_stock(cantidad):
                raise ValueError(f'Stock insuficiente para el producto {producto.nombre}')

        # Si todas las comprobaciones pasan, descontar stock y crear pedido
        for prod_id, cantidad in items:
            producto = self.productos[prod_id]
            producto.actualizar_stock(-cantidad)  # descontar unidades

        # Crear el objeto Pedido usando lookup de productos
        pedido = Pedido(usuario, items, self.productos)
        self.pedidos[pedido.id] = pedido
        return pedido

    def listar_pedidos_por_usuario(self, usuario_id: str) -> List[Pedido]:
        # Devuelve la lista de pedidos filtrada por cliente (ordenados por fecha)
        pedidos_usuario = [p for p in self.pedidos.values() if p.cliente.id == usuario_id]
        # Ordenar por fecha ascendente
        pedidos_usuario.sort(key=lambda p: p.fecha)
        return pedidos_usuario
