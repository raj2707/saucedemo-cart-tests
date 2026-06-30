class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.first_name = page.get_by_test_id("firstName")
        self.last_name = page.get_by_test_id("lastName")
        self.postal = page.get_by_test_id("postalCode")
        self.continue_btn = page.get_by_test_id("continue")
        self.error_msg = page.get_by_test_id("error")

        self.finish_btn = page.get_by_test_id("finish")
        self.summary_total = page.get_by_test_id("total-label")

        self.success_msg = page.get_by_test_id("complete-header")

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