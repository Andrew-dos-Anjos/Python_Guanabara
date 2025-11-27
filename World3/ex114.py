#Site está acessível?
# ----------
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print("O site está inacessível no momento.")
else:
    print("Site acessado com sucesso!")
    print(site.read())  #Pega o html do site
