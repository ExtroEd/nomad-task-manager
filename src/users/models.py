from sqlalchemy.ext.


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id