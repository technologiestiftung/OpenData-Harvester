import settings
from opendata import importer, ckan

apikey = settings.API_KEY
url = settings.API_URL
'''
package = ckan.gather_data('07c6ea8e-2ece-45db-9923-7c23a22f7945', url, apikey)
print(package)
'''
entries = ckan.gatherCity('berlin', url, apikey)
print(entries)

'''
for entry in entries:
    package = ckan.gather_data(entry, url, apikey)
    importer.import_package(package)
'''
