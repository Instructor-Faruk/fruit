from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="postgresql+psycopg2://fruit_db_dt1z_user:0ewcLPfSgnYm9hB0kZvUIUHYAKbwo8BX@dpg-dc3alqfavr4c73errf30-a.ohio-postgres.render.com/fruit_db_dt1z"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
