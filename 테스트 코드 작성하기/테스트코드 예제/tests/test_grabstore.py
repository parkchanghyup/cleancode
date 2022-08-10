from main import GrabStore, Product

# Unit test
def test_show_product(grab_store):
    # given

    product_id = 1

    # when
    product = grab_store.show_product(product_id=product_id)

    # then
    assert product == Product(name="키보드", price=30000)


# Intergration Test
def test_sell_product_well(grab_store):
    product_id = 1
    pre_money = grab_store._money
    product = grab_store.show_product(product_id=product_id)

    _product = grab_store.sell_product(product_id=product_id, money=product.price)

    assert grab_store._money == product.price
    assert not grab_store.show_product(product_id=product_id)
