import os
os.system('clear')
os.system('pkg install sqlmap')
os.system('clear')
os.system('sudo apt install sqlmap')
os.system('clear')
print('''
░██████╗░██████╗░██╗░░░░░███╗░░░███╗░█████╗░██████╗░
██╔════╝██╔═══██╗██║░░░░░████╗░████║██╔══██╗██╔══██╗
╚█████╗░██║██╗██║██║░░░░░██╔████╔██║███████║██████╔╝
░╚═══██╗╚██████╔╝██║░░░░░██║╚██╔╝██║██╔══██║██╔═══╝░
██████╔╝░╚═██╔═╝░███████╗██║░╚═╝░██║██║░░██║██║░░░░░
╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░''')

a = input('coloque o site que voce deseja utilizar:')
os.system('clear')
os.system(('sqlmap {} --dbs').format (a))