# Usuario.py
# Definición de Usuario y subclases Cliente y Administrador con comentarios por línea.

import uuid  # para generar ids únicos
from typing import Optional

class Usuario:
    """Clase base que representa un usuario genérico."""
    def __init__(self, nombre: str, email: str) -> None:
        # Genera un id único para el usuario
        self.id: str = str(uuid.uuid4())  # identificador único del usuario
        self.nombre: str = nombre  # nombre del usuario
        self.email: str = email  # email del usuario

    def is_admin(self) -> bool:
        # Por defecto, un usuario no es administrador
        return False

    def __str__(self) -> str:
        # Representación legible del usuario
        return f"Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')"

class Cliente(Usuario):
    """Usuario que añade dirección postal (cliente de la tienda)."""
    def __init__(self, nombre: str, email: str, direccion: Optional[str] = None) -> None:
        # Llamamos al constructor de la clase base para inicializar id, nombre y email
        super().__init__(nombre, email)
        self.direccion: Optional[str] = direccion  # dirección postal del cliente

    def __str__(self) -> str:
        # Incluye la dirección en la representación si existe
        direccion_text = f", direccion='{self.direccion}'" if self.direccion else ''
        return f"Cliente(id={self.id}, nombre='{self.nombre}', email='{self.email}'{direccion_text})"

class Administrador(Usuario):
    """Usuario con privilegios de administrador."""
    def __init__(self, nombre: str, email: str) -> None:
        # Inicializa como usuario normal
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        # Devuelve True para administradores
        return True

    def __str__(self) -> str:
        # Representación específica de administrador
        return f"Administrador(id={self.id}, nombre='{self.nombre}', email='{self.email}')"
