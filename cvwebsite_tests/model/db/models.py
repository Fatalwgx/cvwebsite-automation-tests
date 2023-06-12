from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship, backref
from cvwebsite_tests.model.db.postgres import Base
from datetime import datetime


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    created_on = Column(TIMESTAMP, nullable=False, default=datetime.now())
    last_login = Column(TIMESTAMP, nullable=True, server_default=None)
