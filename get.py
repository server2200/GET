import os
import socket
import subprocess
import sys
import platform

if os.name != 'nt':
    sys.exit(1)
else:
    pass

def PIP(package=str):
    subprocess.run(['pip', 'install', f"{package}"]) 

try:
    import getpass
    import wmi
except ImportError:
    PIP('wmi')
    PIP('getpass')
    os.execv(sys.executable, [sys.executable] + sys.argv)

def GET(GET=str or None):
    """\
    GET="IP": Returns the IP address of the current Computer.
    GET="PCNAME": Returns the Computer name.
    GET="USER": Returns the User name
    GET="HWID": Returns the Hardware ID (UUID) of the computer.
    """
    if GET=="IP":
        return socket.gethostbyname(socket.gethostname())
    elif GET=="PCNAME":
        return os.environ['COMPUTERNAME']
    elif GET=="HWID":
        if os.name!="nt":
            sys.exit("Windows Only.")
        else:
            return wmi.WMI().Win32_ComputerSystemProduct()[0].UUID if hasattr(wmi.WMI().Win32_ComputerSystemProduct()[0], 'UUID') else None
    elif GET=="USER":
        return getpass.getuser()
    elif GET=="OS":
        return platform.system() + platform.release()
