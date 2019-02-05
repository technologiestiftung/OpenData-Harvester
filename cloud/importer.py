import boto3

from opendata import importer, ckan
import json

def call_step_function():
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn='arn:aws:states:eu-central-1:312231911072:stateMachine:OpendataLoadStateStepFunctionsStateMachine-3OzRc0Gzlk5J'
    )

def load_package(client, data):
    client.invoke(
        FunctionName='opendata-harvester5-production-import',
        Payload = data
    )
    return {}
 
def import_package(package_id, url, apikey):
    package = ckan.gather_data(package_id, url, apikey)
    return importer.import_package(package)