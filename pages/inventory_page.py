
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.products = page.get_by_test_id("inventory-item")
        self.cart_button = page.get_by_test_id("shopping-cart-link")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")
        self.sort_dropdown = page.get_by_test_id("product-sort-container")
        self.product_names = page.get_by_test_id("inventory-item-name")
        self.product_prices = page.get_by_test_id("inventory-item-price")

    def add_product_by_name(self, name):
        product = self.products.filter(has_text=name)
        product.get_by_role("button", name="Add to cart").click()

    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.text_content())

    def go_to_cart(self):
        self.cart_button.click()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    def get_product_names(self):
        return self.product_names.all_text_contents()

    def get_product_prices(self):
        prices = self.product_prices.all_text_contents()
        return [float(price.replace("$", "")) for price in prices]