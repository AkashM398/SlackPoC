import logging

import azure.functions as func

import slack 
import json

client = slack.WebClient(token='xoxp-849182343573-848714638612-883406849655-f8e47be95bf10146e7332ffa91e03741')
users = None

def getUsers():
    users =  client.api_call("users.list")
    channelResponse = client.channels_history(channel='CQZ5CAEVB')
    print(channelResponse)
    conversationsResposne = client.conversations_history(channel='GR47G8UKE')
    print('\n')
    print('\n')
    print(conversationsResposne)
    # while(~users.get('ok')):
    #     continue
    membersJson = users.get('members')
    membersJson = json.dumps(membersJson)
    parsed = json.loads(str(membersJson))
    return channelResponse

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    response = getUsers()
    name1 = None
    # for response in list_response:
    #     try:
    #         print(response['real_name'])
    #     except  :
    #         pass
        
    print('\n')
        #name1 = response['real_name']
    
    return func.HttpResponse(f" {response}!")
    
