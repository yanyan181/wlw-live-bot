import os

from twitter import *
import time

def noticeTwitter(live_list):
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    token = os.getenv('access_token')
    token_secret = os.getenv('access_token_secret')

    t = Twitter(auth=OAuth(consumer_key=consumer_key,consumer_secret=consumer_secret,token=token,token_secret=token_secret))

    for live_info in live_list:
        notice_txt ='新着配信\n【タイトル】'+ live_info['title']+'\n【コミュニティ/ユーザ名】'+live_info['distributor']+'\n【配信開始】'+ live_info['publishedAt'] +'\n'+live_info['liveUrl']
        t.statuses.update(status = notice_txt)
        time.sleep(10)