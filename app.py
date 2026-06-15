
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# पूरा इंटरफेस और डिटेल इसी कोड में है
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Ayra Sharma AI</title>
    <style>
        body { background: #0e1117; color: white; text-align: center; font-family: 'Segoe UI', sans-serif; padding-top: 50px; }
        .avatar { width: 220px; height: 220px; background-image: url('avatar.png'); 
                  background-size: cover; border: 4px solid #ff9a9e; border-radius: 50%; 
                  margin: 20px auto; animation: move 3s infinite alternate; }
        @keyframes move { from { transform: translateY(0px) rotate(-2deg); } to { transform: translateY(15px) rotate(2deg); } }
        h1 { margin-bottom: 5px; color: #ff9a9e; }
        p { color: #888; font-style: italic; }
        input { padding: 10px; width: 250px; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background: #ff9a9e; border: none; border-radius: 5px; cursor: pointer; color: white; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Ayra Sharma</h1>
    <h3>18 Years Old</h3>
    <div class="avatar"></div>
    <p>Created by Mohit Sharma</p>
    <br>
    <input type="text" id="userInput" placeholder="Ask Ayra anything...">
    <button onclick="talk()">Chat with Ayra</button>

    <script>
        function talk() {
            let input = document.getElementById("userInput").value;
            let msg = new SpeechSynthesisUtterance();
            msg.text = "Hello! I am Ayra Sharma, 18 years old. I was created by Mohit Sharma. How can I assist you today?";
            msg.pitch = 1.2;
            msg.rate = 1.0;
            window.speechSynthesis.speak(msg);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
