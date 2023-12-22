import requests
from colorama import Fore as f, Back as b, Style
import random 
import os

try:
	os.system("clear")
except:
	os.system("cls")
	
# BANNER 
print(f.YELLOW + "┌──────────────────o───────────────────┐\n│" + f.RED + "           Creador: " + f.BLUE + "n4ss4u            " + f.YELLOW + "│\n│" + f.RED + "          Script: " + f.BLUE + "MirrorSite          " + f.YELLOW + "│\n│" + f.RED +  "         Version: " + f.BLUE + "v0.1 - 2023         "  + f.YELLOW + "│")
print(f.YELLOW + "├──────────────────o───────────────────┤\n│" + f.RED + "     Introduzca la URL del sitio      " + f.YELLOW + "│\n│" + f.RED + "   Telegram https://t.me/agoralatam   " + f.YELLOW + "│\n├──────────────────────────────────────┘")

website = input(f.YELLOW + "│\n└─[" + f.RED + "MirrorSite" + f.YELLOW +"]>> " + Style.RESET_ALL)

try:
	response = requests.get(website)

except:
	print("\n[!] Error, el sitio no se pudo clonar porque no existe.")



if "response" in locals() and response.status_code == 200:
	name_save_file = website 

	if "https://" in website:
		name_save_file = name_save_file.replace("https://", "")

	elif "http://" in website:
		name_save_file = name_save_file.replace("http://", "")

	# GENERARAR NOMBRE PARA GUARDAR EL ARCHIVO
	name_save_file = name_save_file.replace("/", "")
	name_save_file = name_save_file + str(random.randint(1000, 9999))

	# GURADANDO CONTENIDO EN EL ARCHIVO
	file = open(name_save_file + ".html", "w", encoding="utf-8")
	file.write(str(response.text))
	file.close()

	print(f.RED + "\n[!] El sitio clonado se guardó como: " + name_save_file + ".index" + Style.RESET_ALL)

