import sqlalchemy

import models.meta_helper
import models.tables
import settings

user = settings.DB_USER
password = settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
db = settings.DB_NAME
url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format(user, password, host, port, db)

def get_connection():
    return sqlalchemy.create_engine(url, client_encoding='utf8', connect_args={'connect_timeout': 10})
