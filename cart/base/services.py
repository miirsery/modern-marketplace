from django.db.models import Sum


class BasketСontroller:
    def final_basket_price(self, cart):
        final_price_basket = cart.products.values_list(
            'final_price', flat=True
        ).aggregate(Sum('final_price'))
        cart.final_price_cart = final_price_basket['final_price__sum']
        cart.save()
        return True

    def total_products(self, cart):
        total_products = cart.products.values_list(
            'count_product', flat=True
        ).aggregate(Sum('count_product'))
        cart.total_products = total_products['count_product__sum']
        cart.save()
        return True

    def total_discount_products(self, cart):
        total_discount = cart.products.values_list(
            'final_total_discount', flat=True
        ).aggregate(Sum('final_total_discount'))
        cart.total_discount_price = total_discount[
            'final_total_discount__sum'
        ]
        cart.save()
        return True

    def total_price_not_discount_products(self, cart):
        total_price_not_discount = cart.products.values_list(
            'final_price_not_discount', flat=True
        ).aggregate(Sum('final_price_not_discount'))
        cart.total_not_discount_price = total_price_not_discount[
            'final_price_not_discount__sum'
        ]
        cart.save()
        return True
