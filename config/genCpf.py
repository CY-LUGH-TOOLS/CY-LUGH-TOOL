import random, os
os.system('clear')


a = random.randint(100,765)

b = random.randint(184,345)

c = random.randint(104,376)

d = random.randint(34,87)

X = print(('{}.{}.{}-{}').format (a,b,c,d))


escolha = -1

#escolhas

while escolha < 1 or escolha > 3:
    escolha = int(input("""\033[1;0m

[ 1 ] validar cpf
[ 2 ] voltar ao menu
[SAIR] ENTER

\033[1;34m---> \033[1;0m"""))
    print(''' ''')
    print('')
    print('')
    
# escolha
if escolha == 1:
    exec(open('valiCpf.py', encoding="utf-8").read(), globals())
if escolha == 2:
    exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())