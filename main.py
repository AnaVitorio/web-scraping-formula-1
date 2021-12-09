
import requests 
from bs4 import BeautifulSoup

url = 'https://www.grandepremio.com.br/f1/classificacao/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='table classificacao table-striped')



lista_classificacao = results.find_all('tr')

#Removendo o primeiro elemento da lista que não me interessa
lista_classificacao.pop(0)

lista = []
for item in lista_classificacao:
    lista.append(item.text.split('\n'))

print("Classificação Fórmula 1\n")
for item in lista:
    print("--------------------")
    print("Posição:",item[1])
    print("Piloto:",item[3])
    print("Equipe e Pontos:",item[4])
