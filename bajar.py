import sys

def bajar(archivo):

    arch=open('{}.csv'.format(archivo),'r')
    contenido=arch.readlines()
    nombrerev=contenido[0][0:-1]

    # abre .sh a generar
    archivo = open( nombrerev+'.sh','w')

    # Escribe linea que crea carpeta  añadiendo salto de línea
    archivo.write('mkdir "{}"\n'.format(nombrerev))

    # Cambio a la carpeta creada
    archivo.write('cd "{}"\n'.format(nombrerev))

    for i in range (1,len(contenido)):
        dato1=contenido[i].find(',')
        url=contenido[i][dato1+1:]

        # Escribe linea que descarga la url en archivo
        archivo.write('wget '+url )

    # vuelvo a la carpeta original
    archivo.write('cd ..\n')

    #Cierra el archivo
    archivo.close
    print('Se genero el archivo: {}.sh'.format(nombrerev))

if __name__ == '__main__':
    while True:
        entrada = input('Dame un archivo!! \nOr Kill (me)!! \n>> ')
        if entrada.lower() == 'kill':
            sys.exit()
        else:
            try:
                bajar(entrada)
            except:
                print('Ese link no existe!! Intenta con uno que si!!')
