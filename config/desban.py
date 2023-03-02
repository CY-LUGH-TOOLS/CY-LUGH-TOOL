import smtplib
import email.message
import os
os.system('clear')

#banner
print ('███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░')
print ('████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗')
print ('██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝')
print ('██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗')
print ('██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║')
print ('╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print ('                                                     ')
print ('██████╗░███████╗░██████╗██████╗░░█████╗░███╗░░██╗')
print ('██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║')
print ('██║░░██║█████╗░░╚█████╗░██████╦╝███████║██╔██╗██║')
print ('██║░░██║██╔══╝░░░╚═══██╗██╔══██╗██╔══██║██║╚████║')
print ('██████╔╝███████╗██████╔╝██████╦╝██║░░██║██║░╚███║')
print ('╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝')
print ('                                                     ')

#banner by
print ('█▀▀▄ █░░█ 　 █▀▀ █░░ █▀▀█ █░░█ █▀▀ █▀▀█ ')
print ('█▀▀▄ █▄▄█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ █▀▀ █▄▄▀ ')
print ('▀▀▀░ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ▀▀▀ ▀░▀▀ ')



#auto
print('')
print('ola usuario do script cy lugh, slayer aq, vou voltar a atualizar esse script em breve, adeus!')
print('')
c = input('coloque o seu email:')
print('')
print (''' Ative a verificaçao de duas etapas, apos isso, ative a opçao senha de apps, crie uma senha para o seu email. Agora coloque a senha.''')

print ('')

d = input ('coloque a senha:')

print('')

print ('''tudo pronto, a senha pode ser usada apenas para usar o seu email. Este método e 100% seguro! ''')

print ('')
print('seu email: {}' .format (c))
print('sua senha de email: {}' .format (d))
print('')
a = input('coloque o numero q foi banido:')

#email
def enviar_email():
    corpo_email = f'Olá suporte do whatsapp, meu numero foi banido de forma injusta!!, por meios ilegais. Solicito o desbanimento do mesmo, o numero é {a}'
 
    msg = email.message.Message()
    msg['Subject'] = 'Olá suporte do whatsapp!'
    msg['From'] = f'{c}'
    msg['To'] = 'support@whatsapp.com'
    password = f'{d}'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('o numero sera desbanido em breve.')

enviar_email()