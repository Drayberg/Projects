from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_TOKEN = getenv('TOKEN')
API_URL = getenv('BASE_URL')
import requests


class ApiTelegram:

    def __init__(self):
        self.url = f'{API_URL}{API_TOKEN}'

    def get_update(self):
        endpoint = 'getUpdates'
        url = requests.get(f'{self.url}/{endpoint}')
        api_url = dict(url.json())
        api_url.pop('ok')
        for key, value in api_url.items():
            client_id = value[0]['message']['from']['id']
            return client_id


def main():
    api = ApiTelegram()
    api.get_update()


if __name__ == '__main__':
    main()
