from django.db import models


class Cart(models.Model):
    product_name = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    user_name = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    quantity_goods_in_basket = models.PositiveIntegerField(
        verbose_name='Количество товара',
        default=1,
    )

    def __str__(self):
        return f'{self.user_name}: {self.product_name}'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
