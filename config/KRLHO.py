import smtplib
import email.message
import re


#banner
print('''
██╗███╗░░██╗░██████╗████████╗░█████╗░  
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗  
██║██╔██╗██║╚█████╗░░░░██║░░░███████║  
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║  
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║  
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  

██████╗░░█████╗░███╗░░██╗██╗
██╔══██╗██╔══██╗████╗░██║██║
██████╦╝███████║██╔██╗██║██║
██╔══██╗██╔══██║██║╚████║╚═╝
██████╦╝██║░░██║██║░╚███║██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝''')
print('')
#arte
print('''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
▒░░░░░░░░████████████████████████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████       
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████       █▀▀▄ █░░█ ▄ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ 
████████████████████████████████████████████       █▀▀▄ █▄▄█ ░ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
████████████████████████████████████████████       ▀▀▀░ ▄▄▄█ ▀ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀

''')

print('')


#auto

c = input('coloque o seu email:')
print('')
print (''' Ative a verificaçao de duas etapas, apos isso, ative a opçao senha de apps, crie uma senha para o seu email. Agora coloque a sua senha de email.''')

print ('')

d = input ('coloque a senha:')

print('')

print ('''tudo pronto, a senha pode ser usada apenas para usar o seu email. Este método e 100% seguro! ''')
print('')
print('caso tenha um script pago, tudo sera salvo. Lembre q tu e pobrekkkkkkk')
print('')
input('digite [OK!] para concordar e seguir:')
print('')
a = input('coloque o insta da pessoa q vc quer derrubar:')
print('''
░█████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗
██╔══██╗██║░░░██║██║██╔════╝██╔══██╗██║
███████║╚██╗░██╔╝██║╚█████╗░██║░░██║██║
██╔══██║░╚████╔╝░██║░╚═══██╗██║░░██║╚═╝
██║░░██║░░╚██╔╝░░██║██████╔╝╚█████╔╝██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝''')
print('')
print('ESTE SCRIPT ESTA EM FASE DE TESTES!, POSSIVELMENTE A CONTA NAO SERA BANIDA, ISTO E UM TESTE!')
input('digite [OK!] para concordar e seguir:')

print((''' 
email de ataque: {}
senha de app: {}
usuario atacado: {}''') .format (c , d , a ))
print('')
print('as informações acima estao certas?')
input('aperte enter:')
escolha = -1

while escolha < 1 or escolha > 2:
    escolha = int(input('''
1 = não

2 = sim

sua escolha: '''))

if escolha == 1:
    exec(open('KRLHO.py', encoding="utf-8").read(), globals())

if escolha == 2:
    exec(open('ok.py', encoding="utf-8").read(), globals())



#email
def enviar_email():
    corpo_email = f'Olá suporte do instagram, sou mãe de um menino que foi abusado virtualmente por este usuario {a} meu filho nao foi o unico!! Olhem as denuncias.'
    
 
    msg = email.message.Message()
    msg['Subject'] = f'Olá suporte do instagram!, o usuario {a} esta abusando de crianças!'
    msg['From'] = f'{c}'
    msg['To'] = 'support@instagram.com'
    password = f'{d}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('o usuario sera banido em breve.')

enviar_email()
