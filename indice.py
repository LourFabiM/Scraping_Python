
import urllib, sys
import urllib.request
from bs4 import BeautifulSoup

def bajar(url):
    req = urllib.request.Request(url)
    r   = urllib.request.urlopen(req)
    return BeautifulSoup( r.read() ,"lxml")

def titulo(sopa):
    for sub_heading in sopa.find_all('title'):
        t =  sub_heading.text
        h = t.find('|')
        titulo = t[0:h-1]
        return titulo

def disponibles(sopa, titulo):
    indice = []
    #archivo = ''
    for p in sopa.find_all('p'):
        contenido = p.contents
        for n in range(len(contenido)):
            tag = p.contents[n]
            try:
                if tag.name == 'a' and tag.has_attr('href'):
                    if tag.span.span:
                        indice.append((tag['title'][:9], tag['href']))
                        #archivo += tag['title'][:9] + ', http://magzdb.org' + tag['href'] + '\n'
            except:
                pass
    return indice

def numeros(lista):
    archivo = ''
    #toma una lista de tuplas (año-num, link) con cada numero disponible para descargar
    for d in lista:
        #extrae el link
        link = 'http://magzdb.org' + d[1]
        #lo descarga
        pag = bajar(link)
        #busca el link de descarga del archivo
        for p in pag.find_all('p'):
            contenido = p.contents
            for n in range(len(contenido)):
                tag = p.contents[n]
                try:
                    if tag.name == 'a' and tag.has_attr('href'):
                        archivo += '{}, http://magzdb.org{}\n'.format(d[0], tag['href'][2:])
                except:
                    pass
    return archivo





def indizar(link):
    with open('revista_{}.csv'.format(link), 'w') as text:
        link = 'http://magzdb.org/j/' + link
        soup =  bajar(link)
        tit = titulo(soup)
        text.write(tit + '\n')
        index = disponibles(soup, tit)
        descargar = numeros(index)
        text.write(descargar)




if __name__ == '__main__':
    while True:
        entrada = input('Dame un numero!! \nOr Kill (me)!! \n>> ')
        if entrada.lower() == 'kill':
            sys.exit()
        else:
            try:
                indizar(entrada)
                print('Archivo listo')
            except:
                print('Ese link no es correcto!! Intenta con otro')
