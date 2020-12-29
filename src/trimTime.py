import os
from datetime import datetime,timedelta

def trimTime(call_time , live_list) :
    trim_time = call_time - timedelta(minutes=int(os.getenv('interval')))
    trimed_live_list = []

    for live_item in live_list :
        live_time = datetime.strptime(live_item['publishedAt'], '%Y/%m/%d %H:%M:%S')
        if live_time > trim_time :
            trimed_live_list.append(live_item)
    
    return trimed_live_list