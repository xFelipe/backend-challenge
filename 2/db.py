from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

_config = configparser.ConfigParser()
_config.read('config.ini')

db_url= _config['DATABASE']['DB_URL']
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
