class BasketController():

    def search_product_in_cart(self, cart, prod_obj, new_count_products):
        for item in cart.products.all():
            if prod_obj == item.product_name:
                item.count_product = int(new_count_products)
                item.save()
            else:
                return "There is no such product in the basket"
        return item
