# Crypto Data Pipeline

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![author](https://img.shields.io/badge/author-RafaelGallo-red.svg)](https://github.com/RafaelGallo?tab=repositories) 
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-374/) 
[![](https://img.shields.io/badge/Pandas-blue.svg)](https://pandas.pydata.org/) 
[![](https://img.shields.io/badge/Matplotlib-blue.svg)](https://matplotlib.org/)
[![](https://img.shields.io/badge/Seaborn-green.svg)](https://seaborn.pydata.org/)
[![](https://img.shields.io/badge/SQLite-gray.svg)](https://www.sqlite.org/index.html)
[![](https://img.shields.io/badge/SQLAlchemy-orange.svg)](https://www.sqlalchemy.org/)
[![](https://img.shields.io/badge/PowerBI-yellow.svg)](https://powerbi.microsoft.com/pt-br/)
[![](https://img.shields.io/badge/OpenPyXL-green.svg)](https://openpyxl.readthedocs.io/en/stable/)


![](https://github.com/RafaelGallo/Cript-BTC-USD-Anlytics/blob/main/img/002.png?raw=true)

Este projeto foi desenvolvido para realizar a coleta, armazenamento e análise de dados de criptomoedas, utilizando a API do Yahoo Finance. O pipeline integra Python e SQLite para criar um banco de dados que armazena informações financeiras, que podem ser exportadas para Excel e visualizadas no Power BI.

## **Estrutura do Projeto**

- **`main.py`**: Script principal para criar tabelas no banco e ingerir os dados.
- **`SQL/query.py`**: Script para consultar os dados no banco e exportar resultados para a pasta `output`.
- **`db/`**: Configuração e conexão com o banco SQLite.
- **`models/`**: Definição dos modelos de dados utilizando SQLAlchemy.
- **`services/`**: Serviços para integração com a API do Yahoo Finance.
- **`output/`**: Pasta onde os arquivos gerados (exemplo: Excel) são salvos.
- **`SQL/`**: Scripts SQL e consultas auxiliares.
- **`yahoo_data.db`**: Banco de dados SQLite onde os dados são armazenados.


## **Configuração do Ambiente**

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio


2. **Crie um ambiente virtual e ative-o**:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## **Como Executar**

1. **Criar Tabelas e Ingerir Dados**: 

Execute o script main.py para criar as tabelas no banco e realizar a ingestão de dados:

```bash
python main.py
```

Exemplo de saída:

```bash
Ingestão concluída para BTC-USD. Novos registros inseridos: 3745
```

2. **Consultar Dados e Exportar**

Para consultar os dados e exportar para Excel, execute o script SQL/query.py:

```bash
python SQL/query.py
```

Exemplo de saída:

```bash
Dados exportados com sucesso para 'C:/Case_cadastra/SQL/output/crypto_prices.xlsx'
```

O arquivo será salvo na pasta SQL/output.

## **Resultados no Power BI**

1. Abra o Power BI Desktop.
2. Conecte ao banco de dados SQLite (`yahoo_data.db`) ou importe o arquivo Excel gerado.
3. Crie visualizações dinâmicas, como:
   - Gráficos de linha para preços ao longo do tempo.
   - Gráficos de barras para volumes negociados.
   - Gráficos de velas (Candlestick) para análises detalhadas.

## **Exemplo de Estrutura de Banco**
### **Tabela `crypto_prices`**
| id  | symbol   | date                | open_price | high_price | low_price | close_price | volume   |
|-----|----------|---------------------|------------|------------|-----------|-------------|----------|
| 1   | BTC-USD  | 2024-01-01 00:00:00 | 40000.5    | 41000.0    | 39500.0   | 40500.0     | 120000.0 |

### **Tabela `cryptocurrencies`**
| symbol   | name            |
|----------|-----------------|
| BTC-USD  | Bitcoin         |
| ETH-USD  | Ethereum        |

---

![](https://github.com/RafaelGallo/Cript-BTC-USD-Anlytics/blob/main/img/dash.png?raw=true)

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal.
- **SQLite**: Banco de dados local para armazenamento.
- **SQLAlchemy**: ORM para modelagem e interação com o banco.
- **Pandas**: Manipulação e exportação de dados.
- **openpyxl**: Exportação para Excel.
- **Power BI**: Visualização de dados.

---

## **Contribuição**
Sinta-se à vontade para contribuir com melhorias ou abrir issues para reportar problemas.

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m "Adicionei uma nova feature"
   ```
4. Envie suas mudanças:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.


```
### **Como Usar**

1. Salve o conteúdo acima no arquivo **`README.md`** na raiz do projeto.

2. Faça o commit e o push para o repositório GitHub:

   ```bash
   git add README.md
   git commit -m "Adicionando o README"
   git push origin main
 ```
