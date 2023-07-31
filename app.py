from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from flask_socketio import SocketIO

from DB.database_handler import Database
from user import User

app = Flask(__name__) 
socketio = SocketIO(app)

#app config and DB connections
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root123'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)


#test route for /data using to a get method
@app.route('/data', methods = ['GET'])
def data():

    name = request.args.get('name')
    age = request.args.get('age')
    app.logger.error(age)
    user = User(name, age)
    is_added, error = Database.addUser(mysql, name, age)
    if is_added and not error:
        return 'user added'
    else:
        return 'user not added'
    


#return the home template for commands
@app.route('/', methods=['GET'])
def home():
    message="Start Chatting!"
    return render_template('index.html', 
                           message=message)

#receive the chat ont he event chat
@socketio.on('chat')
def handle_my_custom_event(jsonData):
   
   app.logger.error('received json chat: ' + str(jsonData['data']))
   data = '{"data": "This is new"}'
   socketio.emit('chat', data)


@socketio.on('connection-made')
def handle_connect(jsonData):
    app.logger.error('received json: ' + str(jsonData))
    data = '{"data": "Connection made}'
    socketio.emit('connection-made', data);

if __name__ == '__main__':
    socketio.run(app.run(debug=True))

    