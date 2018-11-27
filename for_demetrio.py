import sys
from indice import indizar
from bajar import bajar

if __name__ == '__main__':
    while True:
        entrada = input('Dame un numero!! \nOr Kill (me)!! \n>> ')
        if entrada.lower() == 'kill':
            sys.exit()
        else:
            try:
#                import pdb; pdb.set_trace()
                indizar(entrada)
                print('Indizando')
                bajar('revista_{}'.format(entrada))
            except:
                print('Intenta con otro')
