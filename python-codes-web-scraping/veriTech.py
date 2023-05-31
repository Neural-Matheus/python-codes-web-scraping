#Basicamente com a biblioteca builtwith iremos verificar qual tecnologia é usada no site para relizarmos um web scraping

#Iremos importar a biblioteca no nosso arquivo.
import builtwith
def verification(site):
    """
    #Uma função que terá o site desejado e retornará as tecnologias resultantes do mesmo.
    """
    tecno = builtwith.parse(site)
    return tecno

siteD = input() # Será a entrada do site desejado, tendo que se necessariamente com todo o link.

print(verification(siteD)) 

