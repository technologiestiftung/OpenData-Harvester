# -*- coding: utf-8 -*-
import models
import requests
import json
import connect
from sqlalchemy.dialects.postgresql import insert

exclude_resource =  ('resource_group_id', 'language', 'webstore_url', 'state', 'webstore_last_updated', 'revision_id', 'apiurl', 'resource_locator_function', 'resource_locator_protocol')
exclude_tag = ('state', 'display_name')
exclude_package =  ('isopen', 'relationships_as_object', 'num_tags', 'num_resources', 'license_url', 'resources', 'groups', 'organization', 'revision_id', 'relationships_as_subject', 'tags', 'extras')
exclude_groups = ('image_display_url')

def exclude_from_dict(d, exclude):
    return {key: d[key] for key in d if key not in exclude}

def insert_or_update(table, entry, unique_id, exclude):
    con = connect.con
    table = models.meta.metadata.tables[table]
    clause = insert(table).values(exclude_from_dict(entry, exclude))
    do_update_clause = clause.on_conflict_do_update(
        index_elements=[unique_id],
        set_=dict(exclude_from_dict(entry, exclude))
    )
    return con.execute(do_update_clause)

def gather_data(package_id, url, apikey):
        urltoread = url + "/api/3/action/package_show?id=" + package_id
        headers = {'Authorization': apikey}
        r = requests.get(urltoread, headers=headers)
        pdata = {}
        try:
            urldata = r.text
            pdata = json.loads(urldata)
        except (RuntimeError, TypeError, NameError, ValueError):
            print('error for url {}'.format(urltoread))
        if 'success' in pdata and pdata['success']:
            return(pdata['result'])

def gatherCity(cityname, url, apikey):
    headers = {'Authorization': apikey}
    r = requests.get(url + "/api/3/action/package_list", headers=headers)
    r.encoding = 'utf-8'
    listpackages = json.loads(r.text)

    return listpackages['result']

def import_package(entry):
    print(entry['type'])
    if entry['type'] == 'harvest':
        return
    print(entry['id'])
    insert_or_update('package', entry, 'id', exclude_package)
    for resource in entry['resources']:
        insert_or_update('resource', resource, 'id', exclude_resource)
    for tag in entry['tags']:
        insert_or_update('tag', tag, 'id', exclude_tag)
    for group in entry['groups']:
        insert_or_update('group', group, 'id', exclude_groups)

