class BasketСontroller:
    def counting_quantity_goods(self, cart):
        quantity_all_products = 0
        queryset_quantity_goods = cart.objects.all().values_list(
            "quantity_goods_in_basket", flat=True
        )
        for item in queryset_quantity_goods:
            quantity_all_products += item
        return quantity_all_products
