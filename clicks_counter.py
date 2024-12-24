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
    response = requests.get('https://api.vk.com/method/utils.getShortLink', 
                            params=params)
    response.raise_for_status()
    short_link = response.json()['response']['short_url']

    return short_link


def count_clicks(link: str, access_key: str) -> int:
    params = {'access_token': access_key,
              'v': '5.199',
              'key': urlparse(link).path[1:],
              'interval': 'forever',
              'extended': 0
              }
    response = requests.get('https://api.vk.com/method/utils.getLinkStats', 
                            params=params)
    response.raise_for_status()
    cliks_count = response.json()['response']['stats'][0]['views']

    return cliks_count


def is_short_link(link: str, access_key: str) ->bool:
    params = {'access_token': access_key,
              'v': '5.199',
              'url': link
              }
    response = requests.get('https://api.vk.com/method/utils.checkLink', 
                            params=params)
    response.raise_for_status()
    return link in response.json()['response']['link']


def main():
    load_dotenv()
    try:
        vk_service_key = os.environ['VK_SERVICE_KEY']
    except KeyError:
        raise RuntimeError('Ключ API VK_SERVICE_KEY не найден!')
    
    link = input('Введите ссылку: ')
    try:
        if is_short_link(link, vk_service_key):
            print('Сокращенная ссылка:', get_short_link(link, vk_service_key))
        else:
            print('Количество кликов: ', count_clicks(link, vk_service_key))
    except (requests.exceptions.RequestException, KeyError, IndexError) as error:
        print('Ошибка: ', error)


if __name__ == '__main__':
    main()