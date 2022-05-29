from django.db.models import Sum


class BasketСontroller:
    def calculation_final_basket_price(self, cart):
        final_price_basket = cart.products.values_list(
            'final_price', flat=True
        ).aggregate(Sum('final_price'))
        cart.final_price_cart = final_price_basket['final_price__sum']
        cart.save()
        return True

    def calculation_total_products(self, cart):
        total_products = cart.products.values_list(
            'count_product', flat=True
        ).aggregate(Sum('count_product'))
        cart.total_products = total_products['count_product__sum']
        cart.save()
        return True
