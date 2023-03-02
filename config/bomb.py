import os
os.system('clear')
print(''' 
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░
█████╗░░██╔████╔██║███████║██║██║░░░░░
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
███████╗██║░╚═╝░██║██║░░██║██║███████╗
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝

██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝''')

print('')
print('antes de tudo, mude as config do script com o nano')
print('')
print('(nano bombEmail.py)')
print('')
print('coloque as informações de ataque e aperte enter apos reiniciar o seu terminal.')
escolha = -1

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0mO que você deseja fazer?
[ 1 ] = iniciar terminal
[ 2 ] = voltar ao menu
[ 99 ] = sair
-----> """))

if escolha == 1:
    exec(open('menu-bomb.py', encoding="utf-8").read(), globals())

if escolha == 2:
    exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())

if escolha == 99:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()