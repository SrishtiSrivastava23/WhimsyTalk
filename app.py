from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Use env var for production
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('chat')
def handle_chat(data):
    # Broadcast the message to all clients
    emit('chat', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
