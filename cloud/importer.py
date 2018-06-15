import boto3

from opendata import importer, ckan
import json

def load_data(city, url, apikey):
    packages = ckan.gatherCity(city, url, apikey)
    for package_id in packages:
        data = json.dumps({
            "package_id": package_id,
            "url": url,
            "api_key": apikey,
        })
        call_lambda(data)
    return {}

def import_package(package_id, url, apikey):
    package = ckan.gather_data(package_id, url, apikey)
    return importer.import_package(package)

def call_step_function(data):
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn='arn:aws:states:eu-central-1:439151911604:stateMachine:Retryfailure',
        input=data
    )

def call_lambda(data):
    client = boto3.client('lambda')
    resp = client.invoke(
            FunctionName='opendata-ckan-dev-import',
            InvocationType = 'Event',
            Payload = data
        )

