# pip install psycopg2-binary

from biodata_registry_api.configs import Settings
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine, text

settings = Settings(
  host="localhost",
  user="user",
  port="5432",
  password="password",
  database="registry"
)

engine = create_engine(
    settings.db_connection_str.replace("+asyncpg", ""),
    echo=True
)
foobar = []
with engine.connect() as connection:
    query = text("SELECT * FROM acquisition_view LIMIT 5;")
    result = connection.execute(query)
    for row in result:
        foobar.append(row)


