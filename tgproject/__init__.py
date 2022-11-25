
import datetime
import re
import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon import functions, types

from telethon.tl.types import InputPeerEmpty, InputMessagesFilterVideo

api_id = 12345678
api_hash = 'qwer1234qwer1234qwer1234qwer1234'


# 
#   Script SETTINGS
#
my_days = 7
my_message_limit = 1000



with TelegramClient('name', api_id, api_hash) as client:
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=500,
        hash=0,
    ))
    

    chat_id = 1234567890
    
    

    channel = client(GetFullChannelRequest(chat_id))
    mes_result = client.get_messages(channel.full_chat, limit=my_message_limit, filter = InputMessagesFilterVideo() )

    week_ago = datetime.date.today() - datetime.timedelta(days=my_days)
    print("Download files between: " + str(week_ago) + " and " + str(datetime.date.today()))
    for res in mes_result:        
        #print(res.date.date()) 

        if(res.date.date() > week_ago):
            filename = "./media_files/" + str(res.date)
            print("-----------> Downloading file: " + str(res.date) + " size: " + str(res.media.document.size), end='')
            res.download_media(file=filename)
            print("   (DONE)")
        else:
            print(str(res.date.date()) + " is not included")


