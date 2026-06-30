
class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_button = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

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