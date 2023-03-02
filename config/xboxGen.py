import random
import string
import os
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

    abc = string.ascii_uppercase

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    d = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=5

        )
    )
)

    abc = string.ascii_uppercase

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    z = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=5

        )
    )
)

    abc = string.ascii_uppercase

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    f = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=5

        )
    )
)

    abc = string.ascii_uppercase

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    g = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=5

        )
    )
)

    abc = string.ascii_uppercase

    numeros = string.octdigits

    ascii_punctuation = abc + numeros

    h = (

    ''.join(

        random. SystemRandom().choices(

            ascii_punctuation,

            k=5

        )
    )
)

    e = ('[ TESTE PARA VER SE FUNCIONA ]')
    print('')
    print(('\033[0;30;32m{}\033[0;30;0m \033[0;30;33m{}-{}-{}-{}-{}').format(e , d, z, f, g, h))
