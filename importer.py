import boto3

import berlin

def load_data(city, url, apikey):
    client = boto3.client('lambda')
    packages = gatherCity(city, url, apikey)
    for package_id in packages:
        resp = client.invoke(
                FunctionName='opendata-berlin-import',
                InvocationType = 'Event',
                Payload =  json.dumps({
                    "package_id": package_id,
                    "url": url,
                    "api_key": apikey,
                })
            )
    return {}

def import_package(package_id, url, apikey):
    package = berlin.gather_data(package_id, url, apikey)
    return berlin.import_package(package)
