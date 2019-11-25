'''
    Making HTTP requests to any number of services has become even more important with all of the networking and 
    cloud solutions out there. 

    Here ia simple example on how to use the requests library to make calls to a RESTful Web Service. The service was created in AWS
    and is also Python based:

    Function Code:

import json

def lambda_handler(event, context):

    returnData = {}


    # Depending on how we are called, we do different things. 
    try:     
        if event['httpMethod'] == 'POST':
            # Load the resquest body     
            bodyobj = json.loads(event["body"])
            responseBodyValue = bodyobj['name'] +  " wishes you well on " + bodyobj["project"]
            returnData["trigger"] = "POST"
            returnData["post_message"] = responseBodyValue
        elif event['httpMethod'] == 'GET':
            returnData["trigger"] = "GET"
            returnData["get_message"] = "A GET occured, should give you something? :)"
        else:
            returnData["trigger"] = event['httpMethod']
    except Exception as ex:
        returnData["exception"] = str(ex)


    return {
        'statusCode': 200,
        'body' : json.dumps(returnData)
    }

'''
import requests 
import json

service_url = 'https://ebqjqw5214.execute-api.us-east-2.amazonaws.com/firstStage/test'
header = {}
header['x-api-key'] = "dJLUvZW8lN3M6xZFWeqcq7I25dxRam785OFvo5mn"


post_request = False
request_result = None

if post_request:
    # Make a POST request
    request_body = {'name': 'Mr. Norton', "project" : "Class Assignment"}
    formatted_body = json.dumps(request_body)
    request_result = requests.post(url = service_url, data = formatted_body, headers = header)
else:
    # Make a GET request
    request_result = requests.get(url = service_url, headers = header)

if request_result :
    # We have some result, so lets print a little bit out. Remember, we know what the 
    # backend code looks like so we know what to look for in the body. 
    print("CALL STATUS -", request_result.status_code)
    result_body = json.loads(request_result.text)
    if post_request :
        print("MESSAGE FOR YOU: " , result_body['post_message'])
    else:
        print("MESSAGE FOR YOU: " , result_body['get_message'])






