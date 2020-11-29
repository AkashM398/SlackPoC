import json, csv

class Entry:

    reply_ts = []
    reply_users = []
    team = 'N/A'
    thread_ts=''
    subtype='N/A'
    reactions_count = 0
    reply_count =0
    parent_ts =''
    users_json =  """[
    {
        "id": "URG3Z1C3C",
        "team_id": "TRUKBGCHW",
        "name": "",
        "deleted": false,
        "color": "3c989f",
        "real_name": "",
        "tz": "Asia\/Kolkata",
        "tz_label": "India Standard Time",
        "tz_offset": 19800,
        "profile": {
            "title": "",
            "phone": "",
            "skype": "",
            "real_name": "",
            "real_name_normalized": "",
            "display_name": "",
            "display_name_normalized": "",
            "fields": null,
            "status_text": "",
            "status_emoji": "",
            "status_expiration": 0,
            "avatar_hash": "b82a9b7e1e15",
            "image_original": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_original.jpg",
            "is_custom_image": true,
            "email": "",
            "image_24": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_24.jpg",
            "image_32": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_32.jpg",
            "image_48": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_48.jpg",
            "image_72": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_72.jpg",
            "image_192": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_192.jpg",
            "image_512": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_512.jpg",
            "image_1024": "https:\/\/avatars.slack-edge.com\/2019-12-19\/879977032896_b82a9b7e1e15ff369139_1024.jpg",
            "status_text_canonical": "",
            "team": "TRUKBGCHW"
        },
        "is_admin": false,
        "is_owner": false,
        "is_primary_owner": false,
        "is_restricted": false,
        "is_ultra_restricted": false,
        "is_bot": false,
        "is_app_user": false,
        "updated": 1576744607
    }
]"""
    #sample json; in production supply actual json 
    jsonString = """[
    {
        "client_msg_id": "5cecc0cc-1dca-4b29-af31-f9bc215ca0a7",
        "type": "message",
        "text": "Getting jdbcconnectionexception while using the access code",
        "user": "URG3Z1C3C",
        "ts": "1576909543.056500",
        "team": "TRUKBGCHW",
        "user_team": "TRUKBGCHW",
        "source_team": "TRUKBGCHW",
        "user_profile": {
            "avatar_hash": "gf6357885a50",
            "image_72": "https:\/\/secure.gravatar.com\/avatar\/f6357885a5041d5193232008e7c8f097.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0004-72.png",
            "first_name": "",
            "real_name": "Eswar",
            "display_name": "",
            "team": "TRUKBGCHW",
            "name": "eswarsaladi041",
            "is_restricted": false,
            "is_ultra_restricted": false
        },
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "=Uhq",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Getting jdbcconnectionexception while using the access code"
                            }
                        ]
                    }
                ]
            }
        ],
        "thread_ts": "1576909543.056500",
        "reply_count": 4,
        "reply_users_count": 4,
        "latest_reply": "1576910127.057500",
        "reply_users": [
            "URWCKPER3",
            "URXPYB5FW",
            "URJNMU3A5",
            "URZ75FMJB"
        ],
        "replies": [
            {
                "user": "URWCKPER3",
                "ts": "1576909695.056600"
            },
            {
                "user": "URXPYB5FW",
                "ts": "1576909788.056800"
            },
            {
                "user": "URJNMU3A5",
                "ts": "1576909861.057000"
            },
            {
                "user": "URZ75FMJB",
                "ts": "1576910127.057500"
            }
        ],
        "subscribed": false
    }
]"""
    def assignAttributes(self):
        list_messages = json.loads((self.jsonString))
        file = open('slack_dump.csv', 'w', newline= '')
        writer = csv.writer(file)
        writer.writerow(['ts', 'channel', 'type', 'subtype',\
                        'user_id', 'user_name', 'user_email', 'team', 'text',\
                        'reply_count', 'reply_users', 'reply_ts', 'parent_ts', 'reactions_count'])
        for message in list_messages:
                self.ts = message["ts"]
                self.userId = message['user']
                self.text = message['text']
                self.type = message['type']
                try:
                    self.subtype = message["subtype"]
                except:
                    pass
                try:
                    self.team = message['team']
                except:
                    pass
                try:
                    self.reply_count = message['reply_count']
                except:
                    pass
                try:
                    self.parent_ts = message['thread_ts']
                except:
                    pass
                try:
                    for reply in message['replies']:
                        self.reply_ts.append(reply['ts'])
                except:
                    pass
                try:
                    for user in message['reply_users']:
                        self.reply_users.append(user)
                except:
                    pass
                try:
                    for reaction in message['reactions']:
                        self.reactions_count += reaction['count'] 
                except:
                    pass
                
                self.fetchUserInfo()
                writer.writerow([self.ts, 'channel', self.type, self.subtype,\
                        self.userId, self.user_name, self.user_email, self.team, self.text,\
                        self.reply_count, self.reply_users, self.reply_ts, self.parent_ts, self.reactions_count])
                
        return 
    
    def fetchUserInfo(self):
        list_users = json.loads((self.users_json))
        for user in list_users:
            if(user['id'] == self.userId):
                self.user_name = user['real_name']
                self.user_email = user['profile']['email']

        
obj = Entry()
obj.assignAttributes()
obj.printAttr()
