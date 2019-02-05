from cloud import importer
from db import connect
import models
import json
from opendata import ckan

def load_data(event, context):
    importer.call_step_function()

    response = {
        "statusCode": 200,
        "body": "load_data: step function initiated"
    }

    return response

def import_package(event, context):
    url = event['iterator']['url']
    apikey = event['iterator']['api_key']
    city = event['iterator']['city_name']
    index = event['iterator']['index']

    packages = ckan.gatherCity(city, url, apikey)

    package_id = packages[index]

    importer.import_package(package_id, url, apikey)

    index += 1

    response = {
        "url":url,
        "api_key":apikey,
        "city_name":city,
        "index": index,
        "continue": index < len(packages)
    }

    return response

def create_db(event, context):
    con = connect.get_connection()
    models.meta_helper.metadata.create_all(con)
    return {
        "statusCode": 200,
        "body": "create_db: database created"
    }

