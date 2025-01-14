import yfinance as yf

def fetch_symbol_history(
    symbol: str = "BTC-USD",
    start: str = None,
    end: str = None,
    period: str = None,
    interval: str = "1d"
):
    """
    Coleta o histórico de preços de um símbolo via Yahoo Finance.
    
    Podemos escolher usar 'start' e 'end' para datas específicas,
    OU 'period' para X dias, meses, etc.
    
    Exemplo de uso:
      fetch_symbol_history(symbol="BTC-USD", start="2012-12-18", end="2024-12-18", interval="1d")
    """
    ticker = yf.Ticker(symbol)
    
    # Se 'start' e 'end' foram fornecidos, usamos esses parâmetros.
    # Caso contrário, se preferir usar 'period', podemos checar.
    if start and end:
        df = ticker.history(start=start, end=end, interval=interval)
    else:
        # Se não vier 'start' e 'end', usamos 'period'. 
        # Se 'period' também for None, definimos algum default, ex. '1mo'
        period = period or "1mo"
        df = ticker.history(period=period, interval=interval)

    df.reset_index(inplace=True)
    return df
