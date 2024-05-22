from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Date, VARCHAR, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

# Строка подключения
pg_db = "postgresql+psycopg2://postgres:popoliz@localhost/guitar_engine"

# Движок SqlAlchemy
engine = create_engine(pg_db)
#создаём базовый класс для моделей
class Base(DeclarativeBase): pass

# создаем модель, объекты которой будут храниться в бд
class Masters(Base):
    __tablename__ = "masters"
    id_masters = Column(Integer, primary_key=True, index=True)
    full_name = Column(VARCHAR(50), nullable=False)
    age = Column(Date)
    level = Column(VARCHAR(20), nullable=False)

class Services(Base):
    __tablename__ = "services"
    id_service = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(30), nullable=False)
    cost = Column(Integer, nullable=False)

class Clients(Base):
    __tablename__ = "clients"
    id_client = Column(Integer, primary_key=True, index=True)
    full_name = Column(VARCHAR(50), nullable=False)
    phone = Column(VARCHAR(15), nullable=False)
    address = Column(VARCHAR(50))

class Instruments(Base):
    __tablename__ = "instruments"
    id_instrument = Column(Integer, primary_key=True, index=True)
    type = Column(VARCHAR(20))
    age = Column(Integer)
    status = Column(VARCHAR(20))

class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id_client"))
    master_id = Column(Integer, ForeignKey("masters.id_masters"))
    service_id = Column(Integer, ForeignKey("services.id_service"))
    instrument_id = Column(Integer, ForeignKey("instruments.id_instrument"))

client = relationship('Clients', back_populates='contract')
master = relationship('Masters', back_populates='contract')
service = relationship('Services', back_populates='contract')
instrument = relationship('Instruments', back_populates='contract')



# создаем таблицы
Base.metadata.create_all(bind=engine)