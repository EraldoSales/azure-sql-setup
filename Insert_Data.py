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
        
        # Lista de filmes para popular a tabela
        filmes = [
            ("O Poderoso Chefão", "The Godfather", "Crime/Drama", 1972),
            ("Um Sonho de Liberdade", "The Shawshank Redemption", "Drama", 1994),
            ("O Senhor dos Anéis: O Retorno do Rei", "The Lord of the Rings: The Return of the King", "Fantasia/Aventura", 2003),
            ("Pulp Fiction: Tempo de Violência", "Pulp Fiction", "Crime/Drama", 1994),
            ("A Lista de Schindler", "Schindler's List", "Drama/História", 1993),
            ("O Cavaleiro das Trevas", "The Dark Knight", "Ação/Crime", 2008),
            ("Forrest Gump: O Contador de Histórias", "Forrest Gump", "Drama/Romance", 1994),
            ("Star Wars: Episódio V - O Império Contra-Ataca", "Star Wars: Episode V - The Empire Strikes Back", "Ficção Científica/Aventura", 1980),
            ("Matrix", "The Matrix", "Ficção Científica/Ação", 1999),
            ("Os Bons Companheiros", "Goodfellas", "Crime/Drama", 1990),
            ("Clube da Luta", "Fight Club", "Drama", 1999),
            ("12 Homens e Uma Sentença", "12 Angry Men", "Drama", 1957),
            ("Interestelar", "Interstellar", "Ficção Científica/Drama", 2014),
            ("Os Infiltrados", "The Departed", "Crime/Drama", 2006),
            ("O Resgate do Soldado Ryan", "Saving Private Ryan", "Guerra/Drama", 1998),
            ("O Rei Leão", "The Lion King", "Animação/Aventura", 1994),
            ("De Volta Para o Futuro", "Back to the Future", "Ficção Científica/Aventura", 1985),
            ("Gladiador", "Gladiator", "Ação/Drama", 2000),
            ("Cidadão Kane", "Citizen Kane", "Drama/Mistério", 1941),
            ("Casablanca", "Casablanca", "Drama/Romance", 1942),
        ]
        
        # Comando para inserir os filmes na tabela
        insert_query = """
        INSERT INTO filmes (nome_port, nome_original, genero, ano_lancamento)
        VALUES (?, ?, ?, ?)
        """
        
        # Inserir cada filme na tabela
        cursor.executemany(insert_query, filmes)
        conn.commit()  # Confirmar as inserções
        
        print("Tabela 'filmes' populada com sucesso!")
        
except pyodbc.Error as e:
    print("Erro ao conectar ou executar o comando:", e)
