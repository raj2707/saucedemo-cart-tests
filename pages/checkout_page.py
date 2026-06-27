# pages/checkout_page.py
class CheckoutPage:

    def __init__(self, page):
        self.page = page
        # Etapa 1 — date personale
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name  = page.locator("[data-test='lastName']")
        self.postal     = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.error_msg  = page.locator("[data-test='error']")
        # Etapa 2 — sumar + finalizare
        self.finish_btn = page.locator("[data-test='finish']")
        self.summary_total = page.locator(".summary_total_label")
        # Confirmare
        self.success_msg = page.locator(".complete-header")

    def fill_details(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal.fill(postal)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()

    def get_total(self):
        return self.summary_total.text_content()

    def get_success_message(self):
        return self.success_msg.text_content()

    def get_error_message(self):
        return self.error_msg.text_content()