import pandas as pd
import numpy as np
import re
import sqlite3 as sql

# csv stored in github to dataframe
def githubusercontent(link):
    csv_link = (link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
    data = pd.read_csv(csv_link)
    return data

# create table then load dataframe to table
def dataframe_to_database(table_name, dataframe):
    dataframe.to_sql(table_name, conn, if_exists = 'replace', index = False)
    print('Table is ready')  

def sql_query(query_file):
    with open(query_file) as f:
        query=(f.read())
    query_statement = f"{query}"
    query_output = pd.read_sql(query_statement, conn)
    print(query_statement)
    print(query_output)


#main

data = githubusercontent('https://github.com/cmotte4git/colab/blob/main/produits.csv')
conn = sql.connect('Stage.db')

# Create table
dataframe_to_database('products', data)

sql_query('query_produits.txt')

