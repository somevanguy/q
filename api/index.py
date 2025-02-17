from flask import Flask, request

app = Flask(__name__)
greetmsg = 'A little thing i made to quickly manage stuff, source code: "https://github.com/somevanguy/q/edit/main/api/index.py"'

@app.route('/')
def home():
    if request.headers.get("User-Agent").find("WindowsPowerShell"):
        return f'Write-Output "{greetmsg}"', 200
    else:
        return greetmsg, 200

@app.route('/noblox')
def about():
    return 'temp'
