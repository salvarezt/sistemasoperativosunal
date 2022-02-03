const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

server.listen(5000, () => {
    console.log('>> Socket escuchando en el puerto 5000')
})

io.on('connection', (socket) => {
    const idHandShake = socket.id;
    const { nameRoom } = socket.handshake.query;

    socket.join(nameRoom);

    console.log(`Hola compañero ${idHandShake} -> ${nameRoom}`)

    socket.on('event', (res) => {
        // socket.to vuelve a emitir la informacion a todos los
        // conectados en la sala EXCEPTO por la persona que emitió la info.
        socket.to(nameRoom).emit('event', res);
    })
})