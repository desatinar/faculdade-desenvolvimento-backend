import sqlite3
import pandas as pd
import os

def csvs_to_sqlite(csv_list, db_name):
    print('Iniciando a criação do banco de dados')
    
    with sqlite3.connect(db_name) as conn:
        for csv_path in csv_list:
            try:
                table_name = os.path.splitext(os.path.basename(csv_path))[0]
                df = pd.read_csv(csv_path)
                df.to_sql(table_name, conn, if_exists='replace', index=False)

                print(f'Tabela {table_name} criada com sucesso')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Ocorreu um erro ao processar o arquivo')

db_file = '../data/clinica.db'
files = [
    '../data/consultas.csv',
    '../data/pacientes.csv',
    '../data/diabetes_id.csv'
]

csvs_to_sqlite(files, db_file)