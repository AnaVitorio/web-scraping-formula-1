
#importando bibliotecas
import requests 
from bs4 import BeautifulSoup

#definindo a url do site, onde serão extraídas as informações
url = 'https://www.grandepremio.com.br/f1/classificacao/'

# Função que irá realizar toda a busca pela url especificada, extraindo as informações solicitadas
def buscar(url):
    page = requests.get(url) #solicitação GET para obter os dados da url
    soup = BeautifulSoup(page.content, 'html.parser') #Armazenando todo o conteúdo da html da página
    #encontrando a classe html onde estão as informações desejadas
    results = soup.find(class_='table classificacao table-striped')
    #Armazenando só as tags com as informações da classificação
    lista_classificacao = results.find_all('tr')
    #Removendo o primeiro elemento da lista que não me interessa
    lista_classificacao.pop(0)

    #Adicionando somente o texto sem as tags html a uma lista
    lista = []
    for item in lista_classificacao:
        lista.append(item.text.split('\n'))
    return lista

#Função que imprime os resultado da classificação
def resultados(lista):
    print("Classificação Fórmula 1\n")
    for item in lista:
        print("--------------------")
        print("Posição:",item[1])
        print("Piloto:",item[3])
        print("Equipe e Pontos:",item[4])

resultados(buscar(url))

