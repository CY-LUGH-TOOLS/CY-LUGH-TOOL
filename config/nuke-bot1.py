#python -m pip install -r requirements.txt
print('''
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░''')
escolha = -1

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0m
[ 1 ] NUKAR!
[ 2 ] instalar
\033[0;30;34m------> """))
    print(''' ''')
    print('')
    print('')
    

if escolha == 1:
    exec(open('nuke-bot.py', encoding="utf-8").read(), globals())
    
if escolha == 2:
    exec(open('installNUKE.py', encoding="utf-8").read(), globals())

