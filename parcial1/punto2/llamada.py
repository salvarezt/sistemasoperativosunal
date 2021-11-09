import socket
import asyncio
import ssl

async def main():
    f = open('buda.txt', 'w') # Archivo donde se escribira

    host, port = 'www.buda.com', 443
    context = ssl.create_default_context()

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente = context.wrap_socket(cliente, server_hostname = host)
    cliente.connect( (host, port) )

    id_mercado = 'btc-clp'

    async def enviar(palabraClave):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente = context.wrap_socket(cliente, server_hostname = host)
        cliente.connect( (host, port) )
        cmd = f'GET /api/v2/markets/{id_mercado}/{palabraClave} HTTP/1.0\r\nHost: www.buda.com\r\n\r\n'
        cliente.send(cmd.encode('utf-8'))
        k = ''
        while True:
            data = cliente.recv(500)
            if len(data) < 1:
                break
            k += data.decode('utf-8')

        k = k.split('\r\n\r\n')[1]
        f.write(f'Lo que ves a continuacion son {palabraClave}:\n')
        f.write(k)
        f.write('\n\n')

    p = await asyncio.gather(enviar('trades'),
        enviar('order_book'),
        enviar('ticker'))
    f.close()
    cliente.close()

asyncio.run(main())
