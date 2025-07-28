# WhimsyTalk
A simple real-time chat app with end-to-end encryption built using Flask, Socket.IO, and CryptoJS

✨ Features
Clean pastel-themed interface

End-to-end AES encryption (client-side)

Real-time chat with WebSockets

Personalized username prompt

“You vs Them” message layout

📁 Project Structure
```

WhimsyTalk/
│
├── app.py                # Flask backend + Socket.IO
├── templates/
│   └── index.html        # Main chat interface
├── static/
│   ├── style.css         # Styling
│   └── img/kawaii.png    # (Optional) background image
```

🚀 Getting Started
1. Install dependencies
```
pip install flask flask-socketio
```

```
pip install eventlet
```
2. Run the app
```
python app.py
```

🔐 Encryption
Messages are encrypted using AES (CryptoJS) before sending.

The shared key is hardcoded (supersecretkey123) in the client.

The server only relays encrypted data — no decryption happens server-side.
