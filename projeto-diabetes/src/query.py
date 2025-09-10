import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'clinica.db')
QUERY_FILE = os.path.join(BASE_DIR, '..', 'queries', 'query.sql')

def run_queries_from_file(db_path, query_file):
    with open(query_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    queries = [q.strip() for q in sql_script.split(';') if q.strip()]
    with sqlite3.connect(db_path) as conn:
        for query in queries:
            try:
                cursor = conn.execute(query)
                results = cursor.fetchall()
                print(f"--- Query ---\n{query}\n--- Resultado ---")
                for row in results:
                    print(row)
            except Exception as e:
                print(f"Erro ao executar: {query}\n{e}")

if __name__ == "__main__":
    run_queries_from_file(DB_PATH, QUERY_FILE)