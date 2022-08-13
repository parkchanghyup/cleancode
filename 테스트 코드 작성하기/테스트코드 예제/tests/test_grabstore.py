import pytest

from main import Product
from unittest import mock

# Unit Test
from tests.conftest import API_URL


def test_show_product(mock_api, grab_store, mock_products):
    #given
    product_id = 1
    mock_product = mock_products[product_id]

    #when
    product = grab_store.show_product(product_id=product_id)

    #then
    assert product == Product(name=mock_product["title"], price=mock_product["price"])

def test_take_money(grab_store):
    price = 100
    pre_money = grab_store._money

    grab_store._take_money(money=price)

    assert grab_store._money == pre_money + price

def test_return_money(grab_store):
    price = 100
    pre_money = grab_store._money

    grab_store._return_money(money=price)

    assert grab_store._money == pre_money - price


def test_take_out_product(mock_api, grab_store, mock_products):
    product_id = 1
    mock_product = mock_products[product_id]

    product = grab_store._take_out_product(product_id=1)

    assert product == Product(name=mock_product["title"], price=mock_product["price"])
    # assert not grab_store._products.get(product_id, None)

# Integration Test
def test_sell_product_well(mock_api, grab_store, mock_products):
    product_id = 1
    # pre_money = grab_store._money

    product = grab_store.show_product(product_id=product_id)
    _product = grab_store.sell_product(product_id=product_id, money=product.price)

    assert grab_store._money == product.price
    # assert not grab_store.show_product(product_id=product_id)

def test_sell_product_not_found(mock_api, grab_store, mock_products):
    product_id = 100

    with pytest.raises(Exception):
        grab_store.sell_product(product_id=product_id, money=0)
