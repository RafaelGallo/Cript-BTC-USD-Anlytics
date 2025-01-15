import sqlite3
import pandas as pd

# Caminho do banco de dados
db_path = r"C:\Users\rafae\Downloads\output\Cript-BTC-USD-Anlytics\SQL\yahoo_data.db"

# Conectar ao banco
conn = sqlite3.connect(db_path)

# Listar as tabelas no banco de dados
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tabelas no banco:", tables)


## Consulta 1: Total de registros por criptomoeda

# Consulta SQL
query = """
SELECT symbol, COUNT(*) AS total_registros
FROM crypto_prices
GROUP BY symbol
ORDER BY total_registros DESC;
"""

# Executar e carregar em um DataFrame
df = pd.read_sql_query(query, conn)
print(df)


## Consulta 2: Preço máximo, mínimo e médio de cada criptomoeda

query = """
SELECT 
    symbol,
    MAX(close_price) AS preco_maximo,
    MIN(close_price) AS preco_minimo,
    AVG(close_price) AS preco_medio
FROM crypto_prices
GROUP BY symbol
ORDER BY preco_maximo DESC;
"""

df = pd.read_sql_query(query, conn)
print(df)

## Consulta 3: Volume total negociado por criptomoeda

query = """
SELECT 
    symbol,
    SUM(volume) AS volume_total
FROM crypto_prices
GROUP BY symbol
ORDER BY volume_total DESC;
"""

df = pd.read_sql_query(query, conn)
print(df)

# Consulta 4: Histórico de preços para uma criptomoeda específica (BTC-USD)

query = """
SELECT 
    date,
    open_price,
    high_price,
    low_price,
    close_price,
    volume
FROM crypto_prices
WHERE symbol = 'BTC-USD'
ORDER BY date ASC;
"""

df = pd.read_sql_query(query, conn)
print(df)

## Consulta 5: Data com maior e menor preço para BTC-USD

query = """
SELECT 
    symbol,
    date,
    close_price
FROM crypto_prices
WHERE symbol = 'BTC-USD' AND (close_price = 
    (SELECT MAX(close_price) FROM crypto_prices WHERE symbol = 'BTC-USD')
    OR close_price = 
    (SELECT MIN(close_price) FROM crypto_prices WHERE symbol = 'BTC-USD'))
ORDER BY close_price DESC;
"""

df = pd.read_sql_query(query, conn)
print(df)


# 
df.to_excel("output/consulta1_total_registros.xlsx", index=False, engine="openpyxl")
print("Consulta exportada com sucesso para 'output/consulta1_total_registros.xlsx'")


# Fechar a conexão
conn.close()
