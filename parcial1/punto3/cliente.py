import socket
import asyncio

host, port = 'localhost', 10000
#context = ssl.create_default_context()

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#cliente = context.wrap_socket(cliente, server_hostname = host)
cliente.connect( (host, port) )

pagina = 'carpeta\pagina.html'

#cmd = f'GET {pagina} Este_es_el_nuevo_contenido'
#cliente.send(cmd.encode())

def enviarComandos():
    print('Que comando deseas enviar:\n')
    print('GET: Obtiene la pagina')
    print('SET texto: Escribe el texto en la pagina, los espacios se escriben con guion bajo _')
    print('END: Desconectarse')
    
    cmd = input()

    if cmd[:3] == 'SET':
        m = 'SET ' + pagina + cmd[3:]
        return m.encode('utf-8')
    else:
        return (cmd + ' ' + pagina).encode('utf-8')

while True:
    cmd = enviarComandos()
    cliente.send(cmd)
    data = cliente.recv(500)
    if len(data) < 1:
        break
    else:
        print(data.decode('utf-8'))

cliente.close()
