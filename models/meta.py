# encoding: utf-8

import datetime

"""SQLAlchemy Metadata and Session object"""
from sqlalchemy import MetaData, and_
import sqlalchemy.orm as orm
from sqlalchemy.orm.session import SessionExtension


__all__ = ['Session', 'engine_is_sqlite', 'engine_is_pg']



# SQLAlchemy database engine. Updated by model.init_model()
engine = None

Session = orm.scoped_session(orm.sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
))

create_local_session = orm.sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


#mapper = Session.mapper
mapper = orm.mapper

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database
metadata = MetaData()


def engine_is_sqlite(sa_engine=None):
    # Returns true iff the engine is connected to a sqlite database.
    return (sa_engine or engine).url.drivername == 'sqlite'


def engine_is_pg(sa_engine=None):
    # Returns true iff the engine is connected to a postgresql database.
    # According to http://docs.sqlalchemy.org/en/latest/core/engines.html#postgresql
    # all Postgres driver names start with `postgres`
    return (sa_engine or engine).url.drivername.startswith('postgres')
