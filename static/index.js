var socket = io();

socket.on('connect', function() {
    socket.emit('connection-made', {data: 'I\'m connected!'});
});

document.getElementById('sendText').addEventListener("click", () => {
    let input = document.getElementById('input');
    let list = document.getElementById('textList');
    let childEle = document.createElement("li");
    childEle.textContent = input.value;
    list.appendChild(childEle);
    socket.emit('chat', {data: input.value});
    input.value = "";
});


socket.on('chat', (data) => {
    let jsonData = JSON.parse(data)
    console.log(jsonData.data);
});
