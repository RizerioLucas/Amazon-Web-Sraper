<h1 align="center"> Amazon Web Scraper </h1>

A coleta de dados web, ou raspagem web, é uma forma de mineração que permite a extração de dados de sites da web convertendo-os em informação estruturada para posterior análise.

## Primeiro começamos instalando as bibliotecas necessárias
- BeautifulSoup
- Selenium

```python
from bs4 import BeautifulSoup 
from selenium import webdriver
```

# Tratando os dados
Para tatar os dados primeiro importe pandas, a lista com os items e o pymysql

```python
import pandas as pd
import pymysql
```
Aqui estou trazendo a lista para ser tratada

```python                                                           
from Amazon_web_scraper import lista
```

Com o pymysql faça a conexão no banco de dados neste caso conectei usando o wamp server
```python
con = pymysql.connect(host ="localhost", database="master",user="root",password="")
```

faça 2 funções 1 para criar a tabela e a outra para inserir na tabela 

Criando a tabela:

```python
def create_table():
    sql = """
    create table if not exists Dados(
    id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Nome LONGTEXT,
    Precos LONGTEXT) CHARACTER SET utf8 COLLATE utf8_general_ci;""" # Colocar o char set em utf8 pra não ter nenhum erro
```
Com o pandas crie o data frame para organizar os dados

```python
df = pd.DataFrame(lista, columns=['Nome', 'Precos'])
```
Insira o data frame na tabela

```python
def insert_table(df):
    with con.cursor() as curs:
        for i in range(0 ,len(df)):
            values = (df['Nome'][i],df['Precos'][i])
            curs.execute("INSERT into Dados(Nome, Precos) values(%s,%s)",values)
            con.commit()
    return print('Insert executado com sucesso')
```
Chamando as funções
```python
create_table()
insert_table(df)
```
# Banco de dados 
![image](https://user-images.githubusercontent.com/106561653/175199843-2e7f8b9e-2780-4d9d-a4da-7fc9209e55cc.png)
