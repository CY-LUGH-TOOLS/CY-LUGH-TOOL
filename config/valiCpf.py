
escolha = -1

#escolhas

while escolha < 1 or escolha > 3:
    escolha = int(input("""\033[1;32m
CPF VALIDO!
\033[1;0m[ 1 ] voltar ao menu
[SAIR] ENTER
\033[1;34m---> """))
    print(''' ''')
    print('')
    print('')
    
# escolha
if escolha == 1:
    exec(open('menuCpf.py', encoding="utf-8").read(), globals())

