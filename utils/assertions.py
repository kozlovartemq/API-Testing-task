import allure


@allure.step('Проверка: в ответе есть токен.')
def assert_token_exists(response):
    response_json = response.json()
    assert 'access_token' in response_json.keys(), f'Ошибка при получении токена.\n{response_json}'


@allure.step('Проверка: код ответа совпадает с ожидаемым.')
def assert_code(response, expected_code: int):
    assert response.status_code == expected_code, f'Wrong response code. ({response.status_code})'


@allure.step('Проверка: текст комментария совпадает с ожидаемым.')
def assert_comment_text(response, expected_comment_text: str):
    response_json = response.json()
    if not response_json['json']['errors']:
        assert response_json['json']['data']['things'][0]['data']['body'] == expected_comment_text, 'Текст комментария не совпал с ожидаемым.'
    else:
        assert False, f'Во время запроса произошла ошибка. {response_json["json"]["errors"]}'


@allure.step('Проверка: Id треда совпадает с ожидаемым.')
def assert_thread_found(response, expected_thread_id: str):
    response_json = response.json()
    if not response_json.get('error'):
        assert response_json['data']['children'][0]['data']['name'] == expected_thread_id, 'Id треда не совпал с ожидаемым.'
    else:
        assert False, f'Во время запроса произошла ошибка. {response_json["error"]}'


@allure.step('Проверка: название сабреддита совпадает с ожидаемым.')
def assert_subreddit_found(response, expected_name_prefixed: str):
    response_json = response.json()
    for children in response_json['data']['children']:
        if children['kind'] == 't5' and children['data']["display_name_prefixed"] == expected_name_prefixed:
            return
    assert False, 'Название сабреддита не совпало с ожидаемым.'

