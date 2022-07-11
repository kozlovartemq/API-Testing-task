import pytest
import allure
from utils.assertions import assert_code, assert_subreddit_found, assert_thread_found


@allure.feature('Тесты поиска')
class TestSearch:
    AUTOCOMPLETE_PATH = 'api/subreddit_autocomplete_v2.json'
    BY_ID_PATH = 'by_id'

    @pytest.mark.positive
    @allure.story('Тест: поиск сабреддита по названию')
    def test_get_to_search_subreddit_via_autocomplete_v2(self, api):
        """GET to search a subreddit"""

        query = 'ApiTest'
        path = f'{self.AUTOCOMPLETE_PATH}?query={query}'
        response = api.get(path=path)

        assert_code(response, 200)
        assert_subreddit_found(response, "r/apiTesting")

    @pytest.mark.positive
    @allure.story('Тест: поиск треда по его id')
    def test_get_to_find_thread_by_id(self, api):
        """GET to find a thread by id"""

        thread_id = "t3_f3dfc6"
        path = f'{self.BY_ID_PATH}/{thread_id}'
        response = api.get(path=path)

        assert_code(response, 200)
        assert_thread_found(response, thread_id)
