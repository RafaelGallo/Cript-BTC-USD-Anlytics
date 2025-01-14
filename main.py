import sys
from db.database import engine, SessionLocal
from models.models import Base, Cryptocurrency, CryptoPrice
from services.yahoo_service import fetch_symbol_history
from datetime import datetime

def create_tables():
    """
    Cria as tabelas definidas no ORM (se ainda não existirem).
    """
    Base.metadata.create_all(bind=engine)

def ingest_data(symbol, start_date=None, end_date=None, period=None, interval="1d"):
    session = SessionLocal()
    try:
        df = fetch_symbol_history(
            symbol=symbol,
            start=start_date,
            end=end_date,
            period=period,
            interval=interval
        )
        
        # A partir daqui, vem a lógica para inserir ou atualizar no banco:
        if df.empty:
            print(f"Nenhum dado retornado para {symbol} no período {start_date} a {end_date}")
            return
        
        # Se quiser, verifique se a cripto já existe e crie se não existir
        crypto = session.query(Cryptocurrency).filter_by(symbol=symbol).first()
        if not crypto:
            crypto = Cryptocurrency(symbol=symbol, name=symbol)
            session.add(crypto)
            session.commit()

        count_inserts = 0
        for _, row in df.iterrows():
            date_value = row["Date"]
            existing_price = (
                session.query(CryptoPrice)
                .filter_by(symbol=symbol, date=date_value)
                .first()
            )

            if existing_price:
                # Atualiza
                existing_price.open_price = row["Open"]
                existing_price.high_price = row["High"]
                existing_price.low_price = row["Low"]
                existing_price.close_price = row["Close"]
                existing_price.volume = row["Volume"]
            else:
                # Insere
                new_price = CryptoPrice(
                    symbol=symbol,
                    date=date_value,
                    open_price=row["Open"],
                    high_price=row["High"],
                    low_price=row["Low"],
                    close_price=row["Close"],
                    volume=row["Volume"],
                )
                session.add(new_price)
                count_inserts += 1

        session.commit()
        print(f"Ingestão concluída para {symbol}. Novos registros inseridos: {count_inserts}")
        
    except Exception as e:
        session.rollback()
        print(f"Erro ao ingerir dados: {e}", file=sys.stderr)
    finally:
        session.close()

def main():
    create_tables()

    # Exemplo: buscar histórico de 12 anos para BTC-USD,
    # de 2012-12-18 a 2024-12-18
    ingest_data(
        symbol="BTC-USD",
        start_date="2012-12-18",
        end_date="2024-12-18",
        interval="1d"
    )

if __name__ == "__main__":
    main()