from flask import Flask, request

app = Flask(__name__)
noroblox = "$ErrorActionPreference= 'silentlycontinue'; $MSRBX = \"$U\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Roblox\"; $RMRBX = 'gci \"$Env:SystemDrive\" -Recurse | where {$_.Name -Like \"*roblox*\"} | rm | Out-Null'; $U = \"$Env:SystemDrive\\Users\\$Env:UserName\\\"; write \"Wiping Roblox off this computer\"; write \"1/3\"; gci \"$U\\Desktop\" -Recurse | where {$_.Name -Like \"*roblox*\"} | rm | Out-Null; gci \"$U\\Downloads\" -Recurse | where {$_.Name -Like \"*roblox*\"} | rm | Out-Null; gci \"$U\\Documents\" -Recurse | where {$_.Name -Like \"*roblox*\"} | rm | Out-Null; gci \"$U\\Videos\" -Recurse | where {$_.Name -Like \"*roblox*\"} | rm | Out-Null; write \"2/3\"; gci \"$U\\AppData\\Local\\Temp\\\" | rm | Out-Null; write \"3/3\"; if (Test-Path \"$U\\AppData\\Local\\Roblox\") { rm \"$U\\AppData\\Local\\Roblox\" | Out-Null }; if (Test-Path \"$U\\AppData\\Local\\Roblox\") { write \"Failed to delete Local/Roblox folder. Press Enter when removed.\"; explorer.exe /select,\"$U\\AppData\\Local\\Roblox\"; Read-Host}; if (Test-Path \"$MSRBX\") { write \"The last folder left requires elevated privilages, please remove it manually. Press Enter when removed.\"; explorer.exe /select,\"$MSRBX\"; Read-Host}; Clear-RecycleBin -Force | Out-Null; write \"Removed Default Roblox Traces. For a complete 100% removal, open powershell with administrator and enter:\"; write \"$RMRBX\"; scb \"$RMRBX\"; write \"Command copied to clipboard. Warning: it might take a very long time.\""

@app.route('/')
def home():
    if "WindowsPowerShell" in request.headers.get("User-Agent"):
        return 'scb -Value "https://github.com/somevanguy/q/edit/main/api/index.py"; write "A little thing i made to quickly manage stuff, source code link copied to clipboard."', 200
    else:
        return 'A little thing i made to quickly manage stuff, source code: <a href="https://github.com/somevanguy/q/edit/main/api/index.py">https://github.com/somevanguy/q/edit/main/api/index.py</a>', 200

@app.route('/rm/roblox')
def remove_roblox():
    if "WindowsPowerShell" in request.headers.get("User-Agent"):
        return noroblox, 200
    else:
        return 'Remove roblox. Code ran in the powershell:<br><span style="white-space: pre;">'+noblox.replace('\\'+'"','"').replace('\\'+'\\','\\')+'</span>'
