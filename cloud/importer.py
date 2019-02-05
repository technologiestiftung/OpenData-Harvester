from dotenv import load_dotenv
load_dotenv()

import os

import boto3

from opendata import importer, ckan
import json

def call_step_function():
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn=os.getenv("STATE_MACHINE")
    )

def load_package(client, data):
    client.invoke(
        FunctionName = os.getenv("SERVICE_NAME") + '-' + os.getenv("SERVICE_STATE") + '-import',
        Payload = data
    )
    return {}
 
def import_package(package_id, url, apikey):
    package = ckan.gather_data(package_id, url, apikey)
    return importer.import_package(package)