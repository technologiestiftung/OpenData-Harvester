# -*- coding: utf-8 -*-
import models
import requests
import json
import connect
import settings

def gatherCity(cityname, url, apikey):
    headers = {'Authorization': apikey}
    r = requests.get(url + "/api/3/action/package_list", headers=headers)
    r.encoding = 'utf-8'
    listpackages = json.loads(r.text)

    listpackages = listpackages['result']

    entries = []

    print 'INFO: the names that follow have had special characters removed'
    for item in listpackages:
        urltoread = url + "/api/3/action/package_show?id=" + item
        headers = {'Authorization': apikey}
        r = requests.get(urltoread, headers=headers)
        pdata = {}
        try:
            urldata = r.text
            pdata = json.loads(urldata)
        except (RuntimeError, TypeError, NameError, ValueError):
            print('error for url {}'.format(urltoread))
        if 'success' in pdata and pdata['success']:
            entries.append(pdata['result'])
            break
        else:
            print 'WARNING: No result - access denied?\n' + metautils.findLcGermanCharsAndReplace(item)
    return entries

exclude_resource =  ('resource_group_id', 'language', 'webstore_url', 'state', 'webstore_last_updated', 'revision_id', 'apiurl')
exclude_tag = ('state', 'display_name')
exclude =  ('isopen', 'relationships_as_object', 'num_tags', 'num_resources', 'license_url', 'resources', 'groups', 'organization', 'revision_id', 'relationships_as_subject', 'tags', 'extras')
exclude_groups = ('image_display_url')

def exclude_from_dict(d, exclude):
    return {key: d[key] for key in d if key not in exclude}

def insert_package(entry):
    package = models.meta.metadata.tables['package']
    clause = package.insert().values(exclude_from_dict(entry, exclude))
    con.execute(clause)

def insert_resource(entry):
    resource = models.meta.metadata.tables['resource']
    clause = resource.insert().values(exclude_from_dict(entry, exclude_resource))
    con.execute(clause)

def insert_tag(entry):
    tags = models.meta.metadata.tables['tag']
    clause = tags.insert().values(exclude_from_dict(entry, exclude_tag))
    result = con.execute(clause)

def insert_group(entry):
    groups = models.meta.metadata.tables['tag']
    clause = groups.insert().values(exclude_from_dict(entry, exclude_groups))
    result = con.execute(clause)

apikey = settings.API_KEY
url = settings.API_URL
entries = gatherCity('berlin', url, apikey)
con = connect.con

for entry in entries:
    insert_package(entry)
    for resource in entry['resources']:
        insert_resource(resource)
    for tag in entry['tags']:
        insert_tag(tag)
    for group in entry['groups']:
        insert_group(group)
