import socket
import os
import asyncio

host, port = 'localhost', 10000

class Server:
    def __init__(self, sock = None):
        if sock == None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.clientes = []
        self.archivos = []
    
    def conexion(self, host, port):
        try:
            self.sock.bind( (host, port) )
            print('Server corriendo\n')
        except os.error:
            print('Hubo un error al conectar. ' + os.error)
    
    def recibirConexion(self):
        conn, addr = self.sock.accept()
        self.clientes.append(conn)
        print('¡Se ha conectado un cliente nuevo!')
        print(f'{addr=}\n')
    
    def manejarPedido(self, cliente):
        # En realidad solamente hay las siguientes posibilidades:
        # comando = 'SAVE ' + narchivo
        # comando = 'GET ' + narchivos
        # comando = 'DEL ' + narchivo
        # Manejaremos cada una de estas posibilidades por separado

        pedido = cliente.recv(100).decode('utf-8').split(' ')
        if pedido[0] == 'SAVE':
            self.pedidoGuardar(cliente, pedido)
        if pedido[0] == 'GET':
            self.pedidoRecibir(cliente, pedido)
        if pedido[0] == 'DEL':
            self.pedidoBorrar(cliente, pedido)
            # Borrarmos el archivo del servidor
        print('Pedido correctamente manejado')
        return 0

    #def pedidoGuardar(self, cliente, pedido):
        
    def pedidoGuardar(self, cliente, pedido):
        print(f'Guardaremos el archivo {pedido[1]}')
        f = open(f'carpetaServer/{pedido[1]}', 'w')
        p = cliente.recv(1024)
        f.write(p.decode('utf-8'))
        f.close()
        mensaje = b'Se ha guardado el archivo correctamente'
        cliente.send(mensaje)
        print('Se ha guardado el archivo correctamente')
    
    def pedidoRecibir(self, cliente, pedido):
        try:
            print(f'enviaremos el archivo {pedido[1]}')
            f = open(f'carpetaServer/{pedido[1]}', 'r')
            mensaje = 'Recibiendo Archivo'.encode('utf-8')
            cliente.send(mensaje)
            archivo = f.read()
            cliente.send(archivo.encode('utf-8'))
            f.close()
            print('¡Archivo enviado correctamente!')
        except FileNotFoundError:
            cliente.send('El archivo que buscas no existe en el servidor :c'.encode('utf-8'))
            return 1
    
    def pedidoBorrar(self, cliente, pedido):
        try:
            os.remove(f'carpetaServer/{pedido[1]}')
            Mensaje = '¡Archivo Eliminado Correctamente!'
            cliente.send(Mensaje.encode('utf-8'))
        except os.error:
            Mensaje = 'Ha habido un error al eliminar: ' + os.error
            cliente.send(Mensaje.encode('utf-8'))
            return 1

server = Server()
server.conexion(host, port)
server.sock.listen(5)

while True:
    server.recibirConexion()
    for i in server.clientes:
        server.manejarPedido(i)
