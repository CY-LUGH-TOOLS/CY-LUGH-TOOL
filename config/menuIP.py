import os
os.system('clear')
#banner
print('''
░██████╗░███████╗░█████╗░  ██╗██████╗░
██╔════╝░██╔════╝██╔══██╗  ██║██╔══██╗
██║░░██╗░█████╗░░██║░░██║  ██║██████╔╝
██║░░╚██╗██╔══╝░░██║░░██║  ██║██╔═══╝░
╚██████╔╝███████╗╚█████╔╝  ██║██║░░░░░
░╚═════╝░╚══════╝░╚════╝░  ╚═╝╚═╝░░░░░''')
#by
print('''
█▀▀▄ █──█ 　 █▀▀ █── █▀▀█ █──█ █▀▀ █▀▀█ 
█▀▀▄ █▄▄█ 　 ▀▀█ █── █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
▀▀▀─ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀──▀ ▄▄▄█ ▀▀▀ ▀─▀▀''')

escolha = -1

#escolhas

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0mentre em contato cmg para que eu faça um script .exe pra vc. Para contato me chame via instagram. @slayerkkk_              
[ 1 ] = sair
[ 2 ] = menu
Sua escolha: """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()

if escolha == 2:
    exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())