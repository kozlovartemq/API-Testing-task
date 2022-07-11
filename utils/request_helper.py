import os
from requests import Session
import allure
from utils.assertions import assert_token_exists


class ApiSession:
    SESSION = Session()

    def __init__(self, base_address):
        self.base_address = base_address
        self.oauth_prefix = "https://oauth."

    @staticmethod
    def check_for_used_requests(response, limit=60):
        """
        Вспамогательная функция, которая проверяет сколько запросов совершено за период времени.
        По умолчанию разрешается использовать 60 запросов в минуту.
        """
        headers = response.headers
        if not headers.get('x-ratelimit-used'):
            return
        attempts = headers['x-ratelimit-used']
        assert int(attempts) <= limit, f"Превышено количество запросов в минуту. " \
                                       f"Лимит сбросится через {headers.get('x-ratelimit-reset')} секунд."

    def login(self):
        prefix = "https://www."
        path = "api/v1/access_token"
        data = {
                "grant_type": "password",
                "username": os.environ.get('REDDIT_USERNAME'),
                "password": os.environ.get('REDDIT_PASSWORD')
                }
        auth = (os.environ.get('REDDIT_CLIENT_ID'), os.environ.get('REDDIT_CLIENT_SECRET'))
        self.SESSION.headers = {"User-Agent": f"Windows:APItest:v0.1 (by /u/{os.environ.get('REDDIT_USERNAME')})"}
        url = f'{prefix}{self.base_address}{path}'
        with allure.step(f'LOGIN (POST request to: {url})'):
            response = self.SESSION.post(url=url, data=data, auth=auth)
            response_json = response.json()
            self.check_for_used_requests(response)
            while 'error' in response_json.keys() and response_json['error'] == 429:  # случай, если вернется ошибка 429: {'message': 'Too Many Requests', 'error': 429}
                response = self.SESSION.post(url=url, data=data, auth=auth)
                response_json = response.json()
                self.check_for_used_requests(response)

        assert_token_exists(response)
        token = response_json['access_token']
        self.SESSION.headers = {'Authorization': f"bearer {token}", **self.SESSION.headers}

    def get(self, path):
        url = f'{self.oauth_prefix}{self.base_address}{path}'
        with allure.step(f'GET request to: {url}'):
            response = self.SESSION.get(url=url)
            self.check_for_used_requests(response)
            return response

    def post(self, path, data=None, json=None):
        url = f'{self.oauth_prefix}{self.base_address}{path}'
        with allure.step(f'POST request to: {url}'):
            response = self.SESSION.post(url=url, data=data, json=json)
            self.check_for_used_requests(response)
            return response

    def put(self, path, data=None):
        url = f'{self.oauth_prefix}{self.base_address}{path}'
        with allure.step(f'PUT request to: {url}'):
            response = self.SESSION.put(url=url, data=data)
            self.check_for_used_requests(response)
            return response

    def delete(self, path, data=None):
        url = f'{self.oauth_prefix}{self.base_address}{path}'
        with allure.step(f'DELETE request to: {url}'):
            response = self.SESSION.delete(url=url, data=data)
            self.check_for_used_requests(response)
            return response
