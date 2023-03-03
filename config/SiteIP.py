import os, time, sys
os.system('cls')
#os.system('clear')
print('''
░██████╗██╗████████╗███████╗  ██╗██████╗░
██╔════╝██║╚══██╔══╝██╔════╝  ██║██╔══██╗
╚█████╗░██║░░░██║░░░█████╗░░  ██║██████╔╝
░╚═══██╗██║░░░██║░░░██╔══╝░░  ██║██╔═══╝░
██████╔╝██║░░░██║░░░███████╗  ██║██║░░░░░
╚═════╝░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝╚═╝░░░░░''')
z = '''BY: SLAYER
Github: https://github.com/CY-LUGH-TOOLS
creator's github: https://github.com/slayerkk

'''

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
a = input('Coloque o site (Ex: www.youtube.com): ')

b = os.system(f'host {a}')

print(b)