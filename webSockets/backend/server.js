const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

server.listen(5000, () => {
    console.log('>> Socket escuchando por el puerto: 5000');
})

io.on('connection', (socket) => {

    const idHandShake = socket.id; // Id de cliente que se acaba de  conectar
    const { nameRoom } = socket.handshake.query;
    
    socket.join(nameRoom);

    console.log(`Hola persona: ${idHandShake} -> ${nameRoom}`);

    socket.on('event', (res) => {
        // console.log(res)

        // socket.to emite los datos de vuelta a todas las personas
        // conectadas a la sala EXCEPTO la persona que inicio
        socket.to(nameRoom).emit('event', res);
    })
})

