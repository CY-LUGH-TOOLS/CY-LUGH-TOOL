import random, string, os
os.system('clear')

while True:

    abc = string.ascii_letters

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    a = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=16

        )
    )
)

    c = ('[ TESTE PARA SABER SE É VALIDO OU NAO! ]')

    b = print(('\033[0;30;31m{}\033[0;30;0m \033[0;30;32mhttp://discord.gift/{}\033[0;30;0m \033[0;30;31m(USE CONTROL + C PARA PARAR DE GERAR!)\033[0;30;0m').format(c , a))



