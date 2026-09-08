class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.add_to_cart_button = page.get_by_role(
            "button",
            name="Add to cart"
        ).first

        self.cart_link = page.locator(".shopping_cart_link")

    def add_first_product_to_cart(self):
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_link.click()