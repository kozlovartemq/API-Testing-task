import pytest
import allure
from utils.assertions import assert_code
from utils.print_helper import print_json


@allure.feature('Тесты получения информации о профиле')
class TestIdentity:
    IDENTITY_PATH = 'api/v1/me'
    IDENTITY_PREFS_PATH = 'api/v1/me/prefs'

    @pytest.mark.positive
    @allure.story('Тест: получить параметры профиля')
    def test_get_identity(self, api):
        """GET the identity of the user"""

        response = api.get(path=self.IDENTITY_PATH)

        assert_code(response, 200)
        print_json(response.json())

    @pytest.mark.positive
    @allure.story('Тест: получить настройки предпочтений профиля')
    def test_get_identity_prefs(self, api):
        """GET the identity of the user"""

        response = api.get(path=self.IDENTITY_PREFS_PATH)

        assert_code(response, 200)
        print_json(response.json())

