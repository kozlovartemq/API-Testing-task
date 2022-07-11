import pytest
from utils.request_helper import ApiSession


@pytest.fixture(scope='session')
def api():
    session = ApiSession(base_address='reddit.com/')
    session.login()
    return session
