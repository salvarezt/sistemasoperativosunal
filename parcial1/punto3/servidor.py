import socket

host, port = 'localhost', 10000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen(5)

def recibeMensaje(cliente, data):
    data = data.split()
    if data[0] == 'GET':
        f = open(data[1], 'r')
        print('Enviando datos')
        cliente.send(('Esto es lo que pediste:\n' + f.read()).encode('utf-8'))
        print('¡Datos enviados con exito!')
        f.close()
        
    elif data[0] == 'SET':
        f = open(data[1], 'r')
        k = []
        for i in f:
            if i[:7] == '    <p>':
                i = i[:7] + data[2].replace('_', ' ') + '</p></body></html>'
            k.append(i)
        f.close()
        print('Escribiendo en el archivo')
        
        f = open(data[1], 'w')
        for i in k:
            f.write(i)
        f.close()

        cliente.send('\n¡Se ha escrito en el archivo con Exito!\n'.encode('utf-8'))

    elif data[0] == 'END':
        cliente.close()
    else:
        cliente.send(b'Formato Incorreto')
        

while True:
    conn, addr = server.accept()
    print(addr)
    data = ''
    while data[:3] != 'END':
        data = conn.recv(250).decode('utf-8')
        recibeMensaje(conn, data)
        
