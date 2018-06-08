import sqlalchemy

import models.meta
import models.tables
import settings

user = settings.DB_USER
password = settings.DB_PASSWORD
host = 'localhost'
port = 5432
db = 'opendata_berlin'
url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format(user, password, host, port, db)
con = sqlalchemy.create_engine(url, client_encoding='utf8')
