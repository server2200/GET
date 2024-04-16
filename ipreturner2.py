import socket
import subprocess
import sys
import os

try:
    import requests
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'requests'], check=True)
    os.execv(sys.executable, [sys.executable] + sys.argv)

def public_ip():
    return requests.get('https://api.ipify.org?format=json').json()['ip']

def private_ip():
    return socket.gethostbyname(socket.gethostname())
