import logging
import pyodbc
import azure.functions as func
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processando GET /filmes")
    try:
        # Conexão com o banco de dados
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.environ['DB_SERVER']};"
            f"DATABASE={os.environ['DB_NAME']};"
            f"UID={os.environ['DB_USER']};"
            f"PWD={os.environ['DB_PASSWORD']}"
        )
        cursor = conn.cursor()
        
        # Consulta para buscar dados da tabela 'filmes'
        cursor.execute("SELECT Id, nome_port, nome_original, genero, ano_lancamento FROM filmes")
        rows = cursor.fetchall()

        # Formatar os dados em uma lista de dicionários
        filmes = [
            {
                "id": row[0],
                "nome_port": row[1],
                "nome_original": row[2],
                "genero": row[3],
                "ano_lancamento": row[4]
            }
            for row in rows
        ]

        # Retornar os dados em formato JSON
        return func.HttpResponse(json.dumps(filmes), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Erro: {str(e)}")
        return func.HttpResponse("Erro ao conectar ao banco", status_code=500)
