# pages/cart_page.py
class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping = page.locator("[data-test='continue-shopping']")

    def get_item_count(self):
        return self.cart_items.count()

    def remove_item_by_name(self, name):
        item = self.page.locator(f".cart_item:has-text('{name}')")
        item.locator("button").click()

    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def proceed_to_checkout(self):
        self.checkout_button.click()