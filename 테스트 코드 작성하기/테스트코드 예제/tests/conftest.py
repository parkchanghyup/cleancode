import pytest

from GrabRealStore import GrabRealStore
from main import GrabStore, Product, User


@pytest.fixture(scope='function')
def mock_products():

    return {
            1:{"title" : "키보드", 'price':30000},  # cheap
            2: {"title" : "냉장고", 'price':500000}  # expensive
        }


# 프로젝트에서 필요한 코드를 모아둔다.
@pytest.fixture(scope="function")
def grab_store():
    return GrabRealStore()



@pytest.fixture(scope="function")
def user(grab_store):
    return User(money=100000, store=grab_store)
