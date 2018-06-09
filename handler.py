import sys, os, json

here = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(here, "./berlin/lib/python2.7/site-packages/")
sys.path.append(env_path)


import importer
import connect
import models

def load_data(event, context):
    city = event['city_name']
    url = event['url']
    apikey = event['api_key']
    importer.load_data(city, url, apikey)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def import_package(event, context):
    package_id = event['package_id']
    url = event['url']
    apikey = event['api_key']
    result = importer.import_package(package_id, url, apikey)
    body = {
        "message": "import for package id",
        "package_id": package_id,
        "input": event,
        "result": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def create_db(event, context):
    models.meta.metadata.create_all(connect.con)

