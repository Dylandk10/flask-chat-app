var socket = io();

socket.on('connect', function() {
    socket.emit('connection-made', {data: 'I\'m connected!'});
});

document.getElementById('sendText').addEventListener("click", () => {
    socket.emit('chat', {data: "Here is message"});
});


socket.on('chat', (data) => {
    console.log(data);
});
