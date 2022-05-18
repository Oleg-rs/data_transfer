import subprocess

subprocess.Popen("server.py", shell=True)
subprocess.call("client.py", shell=True)