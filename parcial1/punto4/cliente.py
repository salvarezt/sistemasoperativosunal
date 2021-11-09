import os
import socket
import asyncio

host, port = 'localhost', 10000

class Cliente:
    def __init__(self, sock = None):
        if sock == None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        
    def conectar(self, host, port):
        try:
            self.sock.connect( (host, port) )
            print('¡Conexion lograda!')
        except os.error:
            print('Hubo un error al conectar. ' + os.error)
    
    def guardarArchivo(self, narchivo = ''):
        # narchivo es el nombre del archivo a guardar en el server
        if narchivo == '':
            print('Debes ingresar un archivo para enviar')
            return 0
        try:
            f = open(f'carpetaCliente/{narchivo}', 'r')
            p = f.read()
            comando = 'SAVE ' + narchivo
            self.sock.send(comando.encode('utf-8')) # Guardar archivo
            self.sock.send(p.encode('utf-8'))

            mensajeRecibido = self.sock.recv(50) # Queremos saber que no hubo problemas para recibir el mensaje
            print(mensajeRecibido.decode('utf-8'))
            f.close()
        except os.error:
            print('Hubo un error al enviar el archivo ' + os.error)
            return 1
    
    def recibirArchivo(self, narchivo = ''):
        # narchivo es el nombre de los archivos a recibir
        if narchivo == '':
            print('No se ha pedido ningun archivo')
            return 0
        elif os.path.exists(f'carpetaCliente/{narchivo}'):
            print('El archivo que intentas recibir ya existe en tu carpeta\nEste archivo sera re-escrito')
        comando = 'GET ' + narchivo
        try:
            self.sock.send(comando.encode('utf-8'))
            f = open(f'carpetaCliente/{narchivo}', 'w')
            mensaje = self.sock.recv(50).decode('utf-8')
            print(mensaje)
            if mensaje != 'Recibiendo Archivo':
                return 1
            temp = self.sock.recv(500).decode('utf-8')
            f.write(temp + '\n')
            print('Archivos recibidos con exito')
            f.close()
            return 0
        except os.error:
            print('Hubo un error al obtener los archivos: ' + os.error)
            return 1

    def eliminarArchivo(self, narchivo = ''):
        if narchivo == '':
            print('Debes ingresar el nombre del archivo a eliminar')
            return 0
        try:
            comando = 'DEL ' + narchivo
            self.sock.send(comando.encode('utf-8'))
            mensajeRecibido = self.sock.recv(50) # Queremos saber que no hubo problemas para eliminar
            print(mensajeRecibido.decode('utf-8'))
            return 0
        except os.error:
            print('Hubo un error eliminando el archivo: ' + os.error)
            return 1

    def desconectar(self):
        self.sock.close()

cliente = Cliente()
cliente.conectar(host, port)
cliente.guardarArchivo('archivo.txt')
cliente.recibirArchivo('pedido.txt')
cliente.eliminarArchivo('borrado.txt')
cliente.desconectar()

