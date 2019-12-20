import logging

import azure.functions as func

import slack 
import json

client = slack.WebClient(token='xoxp-849182343573-848714638612-883406849655-f8e47be95bf10146e7332ffa91e03741')
users = None

def getUsers():
    users =  client.api_call("users.list")
    # while(~users.get('ok')):
    #     continue
    membersJson = users.get('members')
    membersJson = json.dumps(membersJson)
    parsed = json.loads(str(membersJson))
    return parsed

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    list_response = getUsers()
    name1 = None
    for response in list_response:
        try:
            print(response['real_name'])
        except  :
            pass
        
        print('\n')
        #name1 = response['real_name']
    
    return func.HttpResponse(f" {name1}!")
    
