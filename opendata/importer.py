# -*- coding: utf-8 -*-
import models
from db import connect
from sqlalchemy.dialects.postgresql import insert

exclude_resource =  ('resource_group_id', 'language', 'webstore_url', 'state', 'webstore_last_updated', 'revision_id', 'apiurl', 'resource_locator_function', 'resource_locator_protocol')
exclude_tag = ('state', 'display_name')
exclude_package =  ('isopen', 'relationships_as_object', 'num_tags', 'num_resources', 'license_url', 'resources', 'groups', 'organization', 'revision_id', 'relationships_as_subject', 'tags', 'extras')
exclude_groups = ('image_display_url')

def exclude_from_dict(d, exclude):
    if len(exclude) is 0:
        return d
    return {key: d[key] for key in d if key not in exclude}

def insert_or_update(table, entry, unique_id, exclude):
    con = connect.get_connection()
    table = models.meta_helper.metadata.tables[table]
    clause = insert(table).values(exclude_from_dict(entry, exclude))
    do_update_clause = clause.on_conflict_do_update(
        index_elements=[unique_id],
        set_=dict(exclude_from_dict(entry, exclude))
    )
    return con.execute(do_update_clause)

def import_package(entry):
    print(entry['type'])
    if entry['type'] == 'harvest':
        return
    print(entry['id'])
    result = insert_or_update('package', entry, 'id', exclude_package)
    package_id = result.inserted_primary_key[0]
    for resource in entry['resources']:
        result_resource = insert_or_update('resource', resource, 'id', exclude_resource)
    for tag in entry['tags']:
        result_tag = insert_or_update('tag', tag, 'id', exclude_tag)
        insert_or_update('package_tag', {'package_id': package_id, 'tag_id': result_tag.inserted_primary_key[0]}, 'id', [])
    for group in entry['groups']:
        result_group = insert_or_update('group', group, 'id', exclude_groups)
        insert_or_update('package_group', {'package_id': package_id, 'group_id': result_group.inserted_primary_key[0]}, 'id', [])

