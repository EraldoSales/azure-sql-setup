import pyodbc

# Configuração da conexão com o Azure SQL
server = 'storms-server.database.windows.net'
database = 'AdaProject'
username = 'Storms'
password = 'Admin2025!'
driver = '{ODBC Driver 18 for SQL Server}'

# String de conexão com ajuste para o Driver 18
conn_str = f"DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes"

try:
    # Conectar ao banco de dados
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()

        # Dados a serem inseridos, omitindo o 'Id' para que seja gerado automaticamente
        produtos = [
            ('Produto D'),
            ('Produto E'),
            ('Produto F')
        ]
        
        # Inserir os dados na tabela 'produto'
        for produto in produtos:
            cursor.execute("INSERT INTO produto (Nome) VALUES (?)", produto)
        
        # Commit para salvar as alterações
        conn.commit()
        
        print("Dados inseridos com sucesso!")

except pyodbc.Error as e:
    print("Erro ao conectar ou executar o comando:", e)
