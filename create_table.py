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
        
        # Comando para criar a tabela
        create_table_query = """
        CREATE TABLE filmes (
            Id INT PRIMARY KEY IDENTITY(1,1),
            nome_port VARCHAR(200) NOT NULL,
            nome_original VARCHAR(200) NOT NULL,
            genero VARCHAR(100),
            ano_lancamento INT
        );
        """
        cursor.execute(create_table_query)
        print("Tabela 'filmes' criada com sucesso!")
        
except pyodbc.Error as e:
    print("Erro ao conectar ou executar o comando:", e)
