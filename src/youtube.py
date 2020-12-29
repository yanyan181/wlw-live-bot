import os

from apiclient.discovery import build
from datetime import datetime,timedelta

def youtubeSearch():
    
    api_key = os.getenv('youtube_api_key')
    youtube = build('youtube', 'v3', developerKey=api_key)

    search_response = youtube.search().list(
        part='snippet',
        q='ワンダーランドウォーズ OR wonderlandwars OR wlw',
        order='date',
        type='video',
        maxResults=20,
        regionCode='JP',
        eventType='live',
        ).execute()
    recent_live_list=[]
    interval = int(os.getenv('interval'))

    for search_item in search_response['items']:
        # 2020-12-26T12:36:38Z
        published_at=datetime.strptime(search_item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ') + timedelta(hours=9)
        notice_item={
            'title' : search_item['snippet']['title'],
            'distributor' : search_item['snippet']['channelTitle'],
            'liveUrl' : 'https://www.youtube.com/watch?v=' + search_item['id']['videoId'],
            'publishedAt' : published_at.strftime('%Y/%m/%d %H:%M:%S')
        }
        recent_live_list.append(notice_item)
    return recent_live_list