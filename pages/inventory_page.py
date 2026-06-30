
class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.products = page.get_by_test_id("inventory-item")
        self.cart_button = page.get_by_test_id("shopping-cart-link")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.sort_dropdown = page.get_by_test_id("product-sort-container")

    def add_product_by_name(self, name):
        product = self.page.locator(f".inventory_item:has-text('{name}')")
        product.locator("button").click()

    def get_cart_count(self):
        return int(self.cart_badge.text_content())

    def go_to_cart(self):
        self.cart_button.click()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()