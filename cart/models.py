from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Cart(models.Model):
    products = models.ManyToManyField(
        'CartProduct',
        blank=True,
        related_name='products_in_cart',
    )
    user_name = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='products_in_cart_user',
    )
    total_products = models.IntegerField(
        verbose_name='Количество товара',
        default=0,
    )
    final_price_cart = models.IntegerField(
        verbose_name='Общая сумма всех товаров',
        default=0,
    )
    total_discount_price = models.IntegerField(
        verbose_name='Общая сумма скидок',
        default=0,
        null=True,
        blank=True,
    )
    total_not_discount_price = models.IntegerField(
        verbose_name='Общая сумма цен без скидок',
        default=0,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user_name} - корзина {self.id}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class CartProduct(models.Model):
    cart = models.ForeignKey(
        'Cart', verbose_name='Корзина',
        on_delete=models.CASCADE,
        related_name='related_products'
    )
    product_name = models.ForeignKey(
        'product.Product',
        verbose_name='Товар',
        on_delete=models.CASCADE
    )
    count_product = models.IntegerField(
        verbose_name='Количество',
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(2147483647)]
    )
    final_price = models.IntegerField(
        verbose_name='Общая сумма',
        default=0,
    )
    final_total_discount = models.IntegerField(
        verbose_name='Общая сумма скидок в корзине',
        default=0,
    )
    final_price_not_discount = models.IntegerField(
        verbose_name='Общая сумма цен без скидок в корзине',
        default=0,
    )

    class Meta:
        verbose_name = 'Продукт для корзины'
        verbose_name_plural = 'Продукты для корзины'

    def __str__(self):
        return f"{self.product_name} добавлен в коризну - {self.cart}"

    def save(self, *args, **kwargs):
        self.final_price = self.count_product * self.product_name.price_now
        self.final_total_discount = self.count_product *\
            self.product_name.discounted_price
        self.final_price_not_discount = self.count_product *\
            self.product_name.price_old
        super().save(*args, **kwargs)
