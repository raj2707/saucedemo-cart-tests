# tests/test_cart.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

USER = "standard_user"
PASS = "secret_sauce"

def login(page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login(USER, PASS)
    return InventoryPage(page)

# One product + finish order
def test_complete_checkout_one_product(page):
    inv = login(page)
    inv.add_product_by_name("Sauce Labs Backpack")
    assert inv.get_cart_count() == 1

    inv.go_to_cart()
    cart = CartPage(page)
    assert cart.get_item_count() == 1

    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    checkout.fill_details("Robert", "Toiu", "010101")
    checkout.finish_order()

    assert "Thank you" in checkout.get_success_message()

# Multiple products
def test_multiple_products_in_cart(page):
    inv = login(page)
    inv.add_product_by_name("Sauce Labs Backpack")
    inv.add_product_by_name("Sauce Labs Bike Light")
    inv.add_product_by_name("Sauce Labs Bolt T-Shirt")
    assert inv.get_cart_count() == 3

    inv.go_to_cart()
    cart = CartPage(page)
    assert cart.get_item_count() == 3

# Remove product
def test_remove_product_from_cart(page):
    inv = login(page)
    inv.add_product_by_name("Sauce Labs Backpack")
    inv.add_product_by_name("Sauce Labs Bike Light")
    inv.go_to_cart()

    cart = CartPage(page)
    cart.remove_item_by_name("Sauce Labs Bike Light")
    assert cart.get_item_count() == 1
    assert "Sauce Labs Backpack" in cart.get_item_names()

# Empty checkout
def test_checkout_empty_fields(page):
    inv = login(page)
    inv.add_product_by_name("Sauce Labs Backpack")
    inv.go_to_cart()
    CartPage(page).proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details("", "", "")
    assert "First Name is required" in checkout.get_error_message()


# Sorting
def test_sort_products_price_low_to_high(page):
    inv = login(page)

    inv.sort_products("lohi")

    prices = inv.get_product_prices()
    assert prices == sorted(prices)