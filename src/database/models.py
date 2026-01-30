from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    display_name = Column(String, nullable=False)

    tg_account = relationship("TelegramAccount", back_populates="user", uselist=False)
    wa_account = relationship("WhatsAppAccount", back_populates="user", uselist=False)
    ratings = relationship("Rating", back_populates="user")

class TelegramAccount(Base):
    __tablename__ = 'telegram_accounts'
    tg_id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    username = Column(String, nullable=True)

    user = relationship("User", back_populates="tg_account")

class WhatsAppAccount(Base):
    __tablename__ = 'whatsapp_accounts'
    wa_id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="wa_account")

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    
    ratings = relationship("Rating", back_populates="discipline")

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'), nullable=False)
    elo = Column(Float, default=1000.0)

    user = relationship("User", back_populates="ratings")
    discipline = relationship("Discipline", back_populates="ratings")

    __table_args__ = (UniqueConstraint('user_id', 'discipline_id', name='_user_discipline_uc'),)

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'), nullable=False)
    winner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    loser_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    elo_change = Column(Float, nullable=False)