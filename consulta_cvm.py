from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Parte 1 do desafio

codigo = input('Digite o código: ')

def ativo(codigo: str) -> pd.DataFrame:

    geckodriver_path = 'geckodriver.exe'

    options = Options()

    options.add_argument('--headless')  # Sem interface gráfica

    service = Service(executable_path=geckodriver_path)

    driver = webdriver.Firefox(service=service, options=options)

    driver.get('https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CPublicaAtivos.asp')

    search_box = driver.find_element(By.NAME, 'CD_ATIV')
    search_box.send_keys(codigo)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    tabela = driver.find_element(By.XPATH, '//table[@class="BodyPP"]')
    linhas = tabela.find_elements(By.TAG_NAME, 'tr')

    lista_tabelas = []
    for linha in linhas[1:2]:  # Pegamos apenas a segunda linha de cada tabela
        cols = linha.find_elements(By.TAG_NAME, 'td')
        colunas = [col.text.strip() for col in cols]
        lista_tabelas.append(colunas)

    driver.quit()

    colunas = ['Código do Ativo', 'Código ISIN', 'Mercado']
    df_parte1 = pd.DataFrame([(linha[0], linha[1], linha[-1]) for linha in lista_tabelas], columns=colunas)


    return df_parte1

parte_1 = ativo(codigo)
print(parte_1)

# Parte 2 do desafio

with open('codigos.txt', 'r') as file:
    codigos = [linha.strip() for linha in file.readlines()]

lista_txt = []

for codigo in codigos:
    dados = ativo(codigo)
    lista_txt.append(dados)

# A função ativo() retorna um dataframe, então precisamos apenas concatenar os dataframes que estão na lista_txt

df_concatenado = pd.concat(lista_txt, ignore_index=True)

df_concatenado.to_excel('resultado_consulta.xlsx', index=False)

print("Exportado com sucesso!")

