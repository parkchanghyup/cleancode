import pytest

from main import GrabStore, Product, User


# 프로젝트에서 필요한 코드를 모아둔다.
@pytest.fixture(scope="function")
def grab_store():
    return GrabStore(
        products={
            1: Product(name="키보드", price=30000),  # cheap
            2: Product(name="냉장고", price=500000),  # expensive
        }
    )


@pytest.fixture(scope="function")
def user(grab_store):
    return User(money=100000, store=grab_store)
