import os
import urllib.request

from bs4 import BeautifulSoup
from datetime import datetime,timedelta

def openRecSearch(call_time):
    url = 'https://www.openrec.tv/game/iohTQkXSdFP'


    instance = urllib.request.urlopen(url)
    soup = BeautifulSoup(instance, 'html.parser')
    live_items=soup.find_all(class_='js-dotTwoLine c-thumbnailVideo__title js-content__list__popularlive__box')
    time_items=soup.find_all(class_='c-thumbnailVideo__footer__time')
    user_items=soup.find_all(class_='c-thumbnailVideo__header__text__ellipsis__link')
    
    index=0
    recent_live_list=[]
    interval = int(os.getenv('interval'))

    for live_item in live_items:
        if 0<time_items[index].text.find('minutes'):
            published_ago = int(time_items[index].text.split('minutes')[0])
            published_at = call_time - timedelta(minutes=published_ago)
            notice_item={
                'title' : live_item['title'],
                'distributor' : user_items[index].text,
                'liveUrl' : live_item['href'],
                'publishedAt' : published_at.strftime('%Y/%m/%d %H:%M:%S')
            }
            recent_live_list.append(notice_item)
        index += 1
    return recent_live_list