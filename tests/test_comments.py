import pytest
import allure
from utils.assertions import assert_code, assert_comment_text


@allure.feature('Тесты работы с комментариями')
class TestComments:
    DEL_COMMENT_PATH = 'api/del'
    EDIT_COMMENT_PATH = 'api/editusertext'
    COMMENT_PATH = 'api/comment'
    MANUALLY_POSTED_COMMENT_ID = 't1_ifpa5ey'  # вручную оставленный комметарий
    # Для того, чтобы сделать тесты независимыми друг от друга, для изменения и удаления используется вручную оставленный комметарий.

    @pytest.mark.run(order=-3)
    @allure.story('Тест: Оставить комментарий')
    @pytest.mark.parametrize('thread_id', [pytest.param('t3_f3dfc6', marks=pytest.mark.positive),
                                           pytest.param(MANUALLY_POSTED_COMMENT_ID, marks=pytest.mark.positive),
                                           pytest.param('t3_yyyyyyy', marks=(pytest.mark.xfail(reason="Id isn't exists"), pytest.mark.negative))],
                             ids=['comment_a_post', 'reply_on_a_comment', 'invalid_id'])
    def test_post_comment_by_id(self, api, thread_id):
        """POST to comment a thread by id"""

        comment_text = "hello there"
        data = {
            'api_type': 'json',
            'return_rtjson': False,
            'text': comment_text,
            'thing_id': thread_id
        }
        response = api.post(path=self.COMMENT_PATH, data=data)

        assert_code(response, 200)
        assert_comment_text(response, comment_text)

    @pytest.mark.run(order=-2)
    @pytest.mark.positive
    @allure.story('Тест: Изменить существующий комментарий')
    def test_post_to_edit_comment(self, api):
        """POST to edit a comment"""

        comment_new_text = "hello there, edited"
        comment_id = self.MANUALLY_POSTED_COMMENT_ID
        data = {
            'api_type': 'json',
            'return_rtjson': False,
            'text': comment_new_text,
            'thing_id': comment_id
        }
        response = api.post(path=self.EDIT_COMMENT_PATH, data=data)

        assert_code(response, 200)
        assert_comment_text(response, comment_new_text)

    @pytest.mark.run(order=-1)
    @pytest.mark.positive
    @allure.story('Тест: Удалить существующий комментарий')
    def test_post_to_delete_comment(self, api):
        """POST to delete a comment"""

        comment_id = self.MANUALLY_POSTED_COMMENT_ID
        response = api.post(path=self.DEL_COMMENT_PATH, data={'id': comment_id})

        assert_code(response, 200)
