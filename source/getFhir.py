import json
import ast
import os
import boto3
import requests as req
import secretsmanager as sm
from datetime import datetime

def search(list, key):
    for item in list:
        if key in item:
            return item


def save_to_bucket(bucket, path, dataToBeSaved):
    s3 = boto3.resource('s3')
    s3object = s3.Object(bucket, path)
    s3object.put(Body=(bytes(json.dumps(dataToBeSaved).encode('UTF-8'))))


def lambda_handler(event, context):

    #get current region
    runtime_region = os.environ['AWS_REGION']

    # Get my API key
    apiKey = sm.get_secret(runtime_region,'FHIRKeys')
    #print(apiKey)
    #print('This Lambda Function was run in region: ', runtime_region)
    
    # put the POST into a dictionary so that it is usable 
    result = ast.literal_eval(str(event)) 

    listOfItems = []
    for item in result:
        pair = {item['name'] : (item['value'])}
        listOfItems.append(pair)
    
    patientGUIDAsDict = search(listOfItems, 'txtBasic')
    patientGUID = str(patientGUIDAsDict['txtBasic'])
    baseUrl = 'https://syntheticmass.mitre.org/v1/fhir/Patient/'
    fullUrl = baseUrl + patientGUID + '?apikey=' + str(apiKey['APIKey'])
    #print (fullUrl)
    
    # sending get request and saving the response as response object 
    rawData = req.get(url = fullUrl) 
    #print(rawData)
    # extracting data in json format 
    jsonData = rawData.json() 
    
    #print(jsonData)
    bucket = 'dsblodgett-xfer'
    path = patientGUID + '.json'
    save_to_bucket(bucket,path,jsonData)
        
    return { 
        'FHIRServerResponseCode': rawData.status_code,
        'created' : datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 
        'patientGuid': patientGUID, 
        'operation' : 'basic', 
        'len': len(jsonData), 
        'storageloc' : bucket + "/" + path 
    }