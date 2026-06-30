
class CartPage:
    
    def __init__(self, page):
        self.page = page
        self.cart_items = page.get_by_test_id("inventory-item")
        self.checkout_button = page.get_by_test_id("checkout")
        self.continue_shopping = page.get_by_test_id("continue-shopping")
        self.item_names = page.get_by_test_id("inventory-item-name")

    def get_item_count(self):
        return self.cart_items.count()

    def remove_item_by_name(self, name):
        item = self.cart_items.filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def get_item_names(self):
        return self.item_names.all_text_contents()

    def proceed_to_checkout(self):
        self.checkout_button.click()