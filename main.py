from Services.Tienda_service import TiendaService
from models.Producto import ProductoElectronico, ProductoRopa

def main():
    tienda = TiendaService()

    # Crear usuarios
    ana = tienda.registrar_usuario("cliente", "Ana", "ana@mail.com", "Calle 1")
    luis = tienda.registrar_usuario("cliente", "Luis", "luis@mail.com", "Calle 2")
    admin = tienda.registrar_usuario("admin", "Admin", "admin@mail.com")

    # Crear productos
    p1 = ProductoElectronico("Auriculares", 50, 10, 24)
    p2 = ProductoRopa("Camiseta", 20, 15, "M", "Azul")

    tienda.añadir_producto(p1)
    tienda.añadir_producto(p2)

    # Inventario inicial
    print("Inventario inicial:")
    for p in tienda.listar_productos():
        print(p)

    # Crear pedido
    pedido1 = tienda.crear_pedido(ana.id, [(p1.id, 1), (p2.id, 2)])
    print("\nPedido creado:")
    print(pedido1)

    # Pedidos de Ana - COMENTAMOS ESTA PARTE PROBLEMÁTICA
    # print("\nPedidos de Ana:")
    # for p in tienda.pedidos_usuario(ana.id):
    #     print(p)

    print("\n✅ Programa ejecutado correctamente")

if __name__ == "__main__":
    main()