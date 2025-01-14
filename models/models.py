from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Cryptocurrency(Base):
    __tablename__ = "cryptocurrencies"
    
    # Vamos usar o "symbol" como PK, por exemplo "BTC-USD"
    symbol = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    # Você pode incluir mais campos, ex.: rank, market, etc.

    # Relacionamento com a tabela crypto_prices
    prices = relationship("CryptoPrice", back_populates="cryptocurrency")

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, ForeignKey("cryptocurrencies.symbol"))
    date = Column(DateTime, default=datetime.utcnow)

    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Float)

    # Relacionamento inverso com Cryptocurrency
    cryptocurrency = relationship("Cryptocurrency", back_populates="prices")
