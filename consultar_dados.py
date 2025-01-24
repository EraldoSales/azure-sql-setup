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

        # Consulta para selecionar todos os filmes
        cursor.execute("SELECT Id, nome_port, nome_original, genero, ano_lancamento FROM filmes")

        # Buscar os resultados
        filmes = cursor.fetchall()

        # Exibir resultados
        print("Dados na Tabela 'filmes':")
        for filme in filmes:
            print(f"Id: {filme.Id}, Nome (PT): {filme.nome_port}, Nome Original: {filme.nome_original}, Gênero: {filme.genero}, Ano de Lançamento: {filme.ano_lancamento}")
 
except pyodbc.Error as e:
    print("Erro ao conectar ou executar o comando:", e)
