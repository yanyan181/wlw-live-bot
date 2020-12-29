from youtube import youtubeSearch
from openRec import openRecSearch
from tweet import noticeTwitter
from trimTime import trimTime
from datetime import datetime,timedelta

def hello_pubsub(event, context):
    call_time = datetime.datetime.today() + timedelta(hours=9)
    print(call_time.strftime('%Y/%m/%d %H:%M:%S'))

    youtube_list = youtubeSearch()
    openrec_list = openRecSearch(call_time)

    live_list = trimTime(call_time, youtube_list + openrec_list)
    print(live_list)
    noticeTwitter(live_list)