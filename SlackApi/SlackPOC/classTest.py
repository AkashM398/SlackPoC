import json, csv

class Entry:

    reply_ts = []
    reply_users = []
    jsonString = """[
    {
        "type": "message",
        "subtype": "channel_join",
        "ts": "1576678032.000200",
        "user": "URWRFHRFG",
        "text": "<@URWRFHRFG> has joined the channel"
    },
    {
        "type": "message",
        "subtype": "channel_join",
        "ts": "1576686692.003800",
        "user": "URX433RQW",
        "text": "<@URX433RQW> has joined the channel",
        "thread_ts" : "sample",
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
        ]
    }
]"""
    def assignAttributes(self):
        list_messages = json.loads((self.jsonString))
        i = 0
        print(type(list_messages))
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

        return 
    
    def printAttr(self):
        print(self.reply_ts[0])

    def main(self):
        print("wtf")
        
obj = Entry()
obj.assignAttributes()
obj.printAttr()