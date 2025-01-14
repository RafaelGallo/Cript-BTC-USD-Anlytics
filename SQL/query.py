import sqlite3
import pandas as pd

# Caminho para o banco de dados
db_path = "SQL/yahoo_data.db"

# Conectar ao banco
conn = sqlite3.connect(db_path)

# Consulta SQL
query = "SELECT * FROM crypto_prices"
df = pd.read_sql_query(query, conn)

# Exportar para Excel
df.to_excel("./output/crypto_prices.xlsx", index=False, engine="openpyxl")

print("Dados exportados com sucesso para 'SQL/crypto_prices.xlsx'")

# Fechar a conexão
conn.close()
