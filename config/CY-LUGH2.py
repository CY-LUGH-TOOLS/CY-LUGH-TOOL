import os, time, sys
os.system('clear')
#os.system('cls')
#nome
z = '''\033[0;30;34m
░█████╗░██╗░░░██╗  ██╗░░░░░██╗░░░██╗░██████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝  ██║░░░░░██║░░░██║██╔════╝░██║░░██║
██║░░╚═╝░╚████╔╝░  ██║░░░░░██║░░░██║██║░░██╗░███████║
██║░░██╗░░╚██╔╝░░  ██║░░░░░██║░░░██║██║░░╚██╗██╔══██║
╚█████╔╝░░░██║░░░  ███████╗╚██████╔╝╚██████╔╝██║░░██║
░╚════╝░░░░╚═╝░░░  ╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝
\033[0;30;32m
████████╗░█████╗░░█████╗░██╗░░░░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║
░░░██║░░░██║░░██║██║░░██║██║░░░░░██║
░░░██║░░░██║░░██║██║░░██║██║░░░░░╚═╝
░░░██║░░░╚█████╔╝╚█████╔╝███████╗██╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝\033[0;30;0m
\033[0;30;34m[\033[0;35;35m*\033[0;30;34m]\033[0;30;0m\033[0;30;35mPág\033[0;30;33m 2\033[0;30;0m'''
for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0002)


escolha = -1

while escolha < 00 or escolha > 99:
    escolha = int(input("""


\033[0;30;32m[ 1 ]\033[0;30;33m = dnsenum
\033[0;30;32m[ 2 ]\033[0;30;33m = Site IP

\033[0;30;32m[ 99 ]\033[0;30;33m  \033[0;30;31msair\033[0;30;0m \033[0;30;34m ~(CY㉿LUGH!)~ \033[0;30;0m \033[0;30;32m[ 00 ]\033[0;30;33m  \033[0;30;34msuporte\033[0;30;0m

\033[0;30;32m[ 0 ]\033[0;30;33m = pagina anterior

\033[0;30;34m┌──(CY㉿LUGH!)-[~]
└─>\033[0;30;0m """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 0:
    exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())

if escolha == 1:
    exec(open('dnsenum.py', encoding="utf-8").read(), globals())

if escolha == 2:
    exec(open('SiteIP.py', encoding="utf-8").read(), globals())