import configparser
from pathlib import Path

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

file_config = Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB_DEV', 'user')
host = config.get('DB_DEV', 'host')
db_name = config.get('DB_DEV', 'db_name')
password = config.get('DB_DEV', 'password')
port = config.get('DB_DEV', 'port')

url_to_db = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'

engine = create_engine(url_to_db, echo=False, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()
