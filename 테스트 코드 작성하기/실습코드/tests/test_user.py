import pytest

from main import Product

# Unit test
def test_check_money(user):
    cheap_price = 500
    expensive_price = 1000000

    #보통 테스트 함수에서는 하나의 테스트만 진행
    can_buy = user._check_money_enough(price = cheap_price)
    assert can_buy

    can_buy = user._check_money_enough(price = expensive_price)
    assert not can_buy

def test_give_money_cheaper(user):
    price = 500
    pre_money = user._money

    user._give_money(money=price)

    assert user._money == (pre_money - price)

def test_give_money_expensive(user):
    price = 1000000


    with pytest.raises(Exception):
        user._give_money(money = price)


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

def test_take_out_product(grab_store):
    product_id = 1

    product = grab_store._take_out_product(product_id)

    assert product == Product(name = '키보드', price = 30000)
    assert not grab_store._products.get(product_id, None)

def test_sell_product_not_found(grab_store):
    product_id = 100

    with pytest.raises(Exception):
        grab_store.sell_product(product_id = product_id, money = 0)

# Intergration Test
def test_purchase_product_well(user):
    # 1. 유저가 돈을 잘 냈는가?
    # 2. 유저의 주머니에 상품이 들어있는가?
    product_id = 1
    pre_user_money = user._money
    user.belongs = []

    product = user.purchase_product(product_id = product_id)

    assert user.get_money() == pre_user_money - product.price
    assert user.get_belongs() == [product]

def test_purchase_product_expensive(user):
    product_id = 2 # price 500,000

    with pytest.raises(Exception):
        user.purchase_product(product_id = product_id)
