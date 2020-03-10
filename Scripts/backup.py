#Script para backup, python versão 3.x

import shutil
import os

today = date.today()
print(today)

fonte = r"C:\Users\jdsen\OneDrive\Documentos\pastaParaBackup"
destino = r"D:\backup"

arquivos = os.listdir(fonte)
arquivos

arquivos2 = os.listdir(destino)
arquivos2

os.chdir(fonte)

for arquivo in arquivos:
	with open(arquivo) as arq:
		print(arquivo,arq.read())

for arquivo in arquivos:
	if os.path.isfile(arquivo):
		shutil.copy(arquivo, destino)