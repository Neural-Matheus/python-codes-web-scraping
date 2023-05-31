#Basicamente com a biblioteca who-is iremos verificar quem é o dono/empresa do site que desejamos fazer web scraping.

import whois #Importando a biblioteca.

def veriOwwner(site):
    """
        Faz a análise do site requisitado.
    """
    info = whois.whois(site)
    return info

siteA = input()
print(veriOwwner(siteA))