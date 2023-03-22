import pandas as pd
from Amazon_web_scraper import lista
import pymysql

#Conectando com o banco de dados
con = pymysql.connect(host ="localhost", database="master",user="root",password="")

# criando a tabela no banco
def create_table():
    sql = """
    create table if not exists Dados(
    id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Nome LONGTEXT,
    Precos LONGTEXT) CHARACTER SET utf8 COLLATE utf8_general_ci;""" # Colocar o char set em utf8 pra não ter nenhum erro

    with con.cursor() as curs:
        curs.execute(sql)
        con.commit()
    return print('Tabela criada com sucesso')


# Transformando os items da lista em um data frame 
df = pd.DataFrame(lista, columns=['Nome', 'Precos'])

# inserindo a tabela no banco
def insert_table(df):
    with con.cursor() as curs:
        for i in range(0 ,len(df)):
            values = (df['Nome'][i],df['Precos'][i])
            curs.execute("INSERT into Dados(Nome, Precos) values(%s,%s)",values)
            con.commit()
    return print('Insert executado com sucesso')



create_table()

insert_table(df)
