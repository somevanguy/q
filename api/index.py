from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    if "WindowsPowerShell" in request.headers.get("User-Agent"):
        return 'scb -Value "https://github.com/somevanguy/q/edit/main/api/index.py"; write "A little thing i made to quickly manage stuff, source code link copied to clipboard."', 200
    else:
        return 'A little thing i made to quickly manage stuff, source code: <a href="https://github.com/somevanguy/q/edit/main/api/index.py">https://github.com/somevanguy/q/edit/main/api/index.py</a>', 200

@app.route('/noblox')
def about():
    return 'temp'
