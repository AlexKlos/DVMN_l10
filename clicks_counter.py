import json
import os

from dotenv import load_dotenv
from urllib.parse import urlparse
import requests


def get_short_link(link: str, access_key: str) -> str:
    params = {'access_token': access_key,
              'v': '5.199',
              'url': link,
              'private': 0
              }
    try:
        response = requests.get('https://api.vk.com/method/utils.getShortLink', 
                                params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)

    try:
        short_link = json.loads(response.text)['response']['short_url']
    except:
        short_link = None
        print('Ошибка: ', json.loads(response.text)['error'])

    return short_link


def count_clicks(link: str, access_key: str) -> int:
    params = {'access_token': access_key,
              'v': '5.199',
              'key': urlparse(link).path[1:],
              'interval': 'forever',
              'extended': 0
              }
    try:
        response = requests.get('https://api.vk.com/method/utils.getLinkStats', 
                                params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print('Ошибка:', error)

    try:
        cliks_count = json.loads(response.text)['response']['stats'][0]['views']
    except:
        cliks_count = None
        print('Ошибка: ', json.loads(response.text)['error'])

    return cliks_count


def is_short_link(link: str) ->bool:
    return True if urlparse(link).netloc == 'vk.cc' else False    


def main():
    load_dotenv()
    VK_SERVICE_KEY = os.getenv('VK_SERVICE_KEY')
    
    link = input('Введите ссылку: ')
    if is_short_link(link):
        print('Количество кликов: ', count_clicks(link, VK_SERVICE_KEY))
    else:
        print('Сокращенная ссылка:', get_short_link(link, VK_SERVICE_KEY))


if __name__ == '__main__':
    main()