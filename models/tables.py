import vdm.sqlalchemy
from sqlalchemy.orm import relation
from sqlalchemy import types, Column, Table, ForeignKey, and_, UniqueConstraint
import datetime

import meta
import types as _types

PACKAGE_NAME_MAX_LENGTH = 100
PACKAGE_NAME_MIN_LENGTH = 2
PACKAGE_VERSION_MAX_LENGTH = 100

MAX_TAG_LENGTH = 100
MIN_TAG_LENGTH = 2

VOCABULARY_NAME_MIN_LENGTH = 2
VOCABULARY_NAME_MAX_LENGTH = 100

package_table = Table('package', meta.metadata,
        Column('id', types.UnicodeText, primary_key=True, default=_types.make_uuid),
        Column('name', types.Unicode(PACKAGE_NAME_MAX_LENGTH),
               nullable=False, unique=True),
        Column('title', types.UnicodeText),
        Column('version', types.Unicode(PACKAGE_VERSION_MAX_LENGTH)),
        Column('url', types.UnicodeText),
        Column('author', types.UnicodeText),
        Column('author_email', types.UnicodeText),
        Column('maintainer', types.UnicodeText),
        Column('maintainer_email', types.UnicodeText),
        Column('notes', types.UnicodeText),
        Column('license_id', types.UnicodeText),
        Column('type', types.UnicodeText, default=u'dataset'),
        Column('owner_org', types.UnicodeText),
        Column('creator_user_id', types.UnicodeText),
        Column('metadata_created', types.DateTime, default=datetime.datetime.utcnow),
        Column('metadata_modified', types.DateTime, default=datetime.datetime.utcnow),
        Column('private', types.Boolean, default=False),
)

resource_table = Table(
    'resource', meta.metadata,
    Column('id', types.UnicodeText, primary_key=True,
           default=_types.make_uuid),
    Column('package_id', types.UnicodeText,
           ForeignKey('package.id')),
    Column('url', types.UnicodeText, nullable=False),
    Column('format', types.UnicodeText),
    Column('description', types.UnicodeText),
    Column('hash', types.UnicodeText),
    Column('position', types.Integer),

    Column('name', types.UnicodeText),
    Column('resource_type', types.UnicodeText),
    Column('mimetype', types.UnicodeText),
    Column('mimetype_inner', types.UnicodeText),
    Column('size', types.BigInteger),
    Column('created', types.DateTime, default=datetime.datetime.utcnow),
    Column('last_modified', types.DateTime),
    Column('cache_url', types.UnicodeText),
    Column('cache_last_updated', types.DateTime),
    Column('url_type', types.UnicodeText),
    Column('extras', _types.JsonDictType),
)

tag_table = Table('tag', meta.metadata,
    Column('id', types.UnicodeText, primary_key=True, default=_types.make_uuid),
    Column('name', types.Unicode(MAX_TAG_LENGTH), nullable=False),
    Column('vocabulary_id',
        types.Unicode(VOCABULARY_NAME_MAX_LENGTH))
)

package_tag_table = Table('package_tag', meta.metadata,
    Column('id', types.UnicodeText, primary_key=True, default=_types.make_uuid),
    Column('package_id', types.UnicodeText, ForeignKey('package.id')),
    Column('tag_id', types.UnicodeText, ForeignKey('tag.id')),
    )


