class BasketController():

    def search_product_in_cart(self, cart, prod_obj, new_count_products):
        """
        Нахождение нужного товара в корзине
        """

        desired_product = cart.products.get(product_name_id=prod_obj)
        
        if desired_product:
            desired_product.count_product = int(new_count_products)
            desired_product.save()
            return desired_product
        else:
            return "There is no such product in the basket"
