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
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝\033[0;30;0m'''


for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

print('')
print('ESTA E UMA TOOL DE CODE ABERTO, ELA ESTA SEMPRE ATUALIZANDO, CASO QUEIRA ADD UMA TOOL ENTRE EM CONTATO CMG VIA INSTAGRAM! @slayerkk_')
print('')
escolha = -1
#\033[0;30;32m[ 13 ]\033[0;30;33m = gerador de gift xbox
#escolhas

while escolha < 00 or escolha > 99:
    escolha = int(input("""
\033[0;30;32m[ 1 ]\033[0;30;33m = DoS (by: palahsu)                       \033[0;30;32m[ 9 ]\033[0;30;33m = bot nuker discord \033[0;30;31m [ OFF ] \033[0;30;0m
\033[0;30;32m[ 2 ]\033[0;30;33m = sqlmap                                  \033[0;30;32m[ 10 ]\033[0;30;33m = puxa ip
\033[0;30;32m[ 3 ]\033[0;30;33m = brutalforce                             \033[0;30;32m[ 11 ]\033[0;30;33m = dowloader YT (linux debian)
\033[0;30;32m[ 4 ]\033[0;30;33m = rapidscan                               \033[0;30;32m[ 12 ]\033[0;30;33m = gerador de nitro
\033[0;30;32m[ 5 ]\033[0;30;33m = banir numero (whatsapp)                 \033[0;30;32m[ 13 ]\033[0;30;33m = gerador de gift xbox
\033[0;30;32m[ 6 ]\033[0;30;33m = desbanir numero (whatsapp)              \033[0;30;32m[ 14 ]\033[0;30;33m = PyPhisher
\033[0;30;32m[ 7 ]\033[0;30;33m = email spammer                           \033[0;30;32m[ 15 ]\033[0;30;33m = nmap
\033[0;30;32m[ 8 ]\033[0;30;33m = gerador de cpf                          \033[0;30;32m[ 16 ]\033[0;30;33m = Net Atack

\033[0;30;32m[ 99 ]\033[0;30;33m  \033[0;30;31msair\033[0;30;0m \033[0;30;34m ~(CY㉿LUGH!)~ \033[0;30;0m \033[0;30;32m[ 00 ]\033[0;30;33m  \033[0;30;34msuporte\033[0;30;0m

\033[0;30;32m[ 0 ]\033[0;30;33m = Proxima pagina \033[0;30;32m[\033[0;30;0m\033[0;30;35mNEW!\033[0;30;0m\033[0;30;32m]\033[0;30;0m

\033[0;30;34m┌──(CY㉿LUGH!)-[~]
└─>\033[0;30;0m """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 0:
    exec(open('CY-LUGH2.py', encoding="utf-8").read(), globals())

if escolha == 1:
    exec(open('DDOS2.py', encoding="utf-8").read(), globals())
    

elif escolha == 2:
    exec(open('SQLI.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('brute.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('RPD1.py', encoding="utf-8").read(), globals())

if escolha == 5:
    exec(open('ban.py', encoding="utf-8").read(), globals())

if escolha == 6:
    exec(open('desban.py', encoding="utf-8").read(), globals())

if escolha == 7:
    exec(open('bomb.py', encoding="utf-8").read(), globals())

if escolha == 8:
    exec(open('menuCpf.py', encoding="utf-8").read(), globals())
    
if escolha == 9:
    exec(open('nuke-bot1.py', encoding="utf-8").read(), globals())

if escolha == 10:
    exec(open('menuIP.py', encoding="utf-8").read(), globals())

if escolha == 11:
    exec(open('YTDOW.py', encoding="utf-8").read(), globals())

if escolha == 12:
    exec(open('GEN-NITRO.py', encoding="utf-8").read(), globals())

if escolha == 13:
    exec(open('XboxMenu.py', encoding="utf-8").read(), globals())

if escolha == 14:
    exec(open('pyphisher.py', encoding="utf-8").read(), globals())

if escolha == 15:
    exec(open('nmap.py', encoding="utf-8").read(), globals())

if escolha == 16:
    exec(open('DerrubaNet.py', encoding="utf-8").read(), globals())


if escolha == 00:
    exec(open('suporte.py', encoding="utf-8").read(), globals())


if escolha == 99:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()
else:
    print('')

#copia nn skiddie!