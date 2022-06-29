from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from autoslug import AutoSlugField


class Product(models.Model):

    STATUS_PRODUCT = [
        ('Have', 'Есть в наличии'),
        ('Havent', 'Временно отсутвует'),
    ]

    title = models.CharField(
        verbose_name='Название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price_now = models.IntegerField(
        verbose_name='Цена в текущий момент',
        blank=True,
        null=True,
    )
    price_old = models.IntegerField(
        verbose_name='Старая цена',
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(2147483647)]
    )
    discounted_price = models.IntegerField(
        verbose_name='Скидка',
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(2147483647)]
    )
    slug = AutoSlugField(
        populate_from='title'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )
    moderation = models.BooleanField(
        verbose_name='Прошло модерацию',
        default=False,
    )
    guarantee = models.PositiveIntegerField(
        verbose_name='Гарантия',
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Товаров в наличии',
        default=0,
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        default=2022,
        validators=[MinValueValidator(2022), MaxValueValidator(2040)]
    )
    status = models.CharField(
        verbose_name='Статус товара',
        choices=STATUS_PRODUCT,
        default='Havent',
        max_length=120,
    )
    photo = models.ManyToManyField(
        'ProductImage',
        verbose_name='Фотографии',
        related_name='product_photos'
    )
    category = models.ForeignKey(
        'Category', verbose_name='Категория',
        on_delete=models.PROTECT,
        related_name='category_product',
    )
    colors = models.ManyToManyField(
        'ProductColor',
        verbose_name='Цвета',
        related_name='product_colors',
        blank=True,
    )
    characteristics = models.JSONField(null=True,)
    favorite_product = models.ManyToManyField(
        'user.User',
        default=None,
        blank=True,
        verbose_name='Добавить в избранное',
        related_name='favorite_products'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'product_detail', kwargs={'product_detail_slug': self.slug}
        )

    def save(self, *args, **kwargs):
        self.price_now = self.price_old - self.discounted_price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    category_name = models.CharField(
        verbose_name='Категория',
        max_length=120
    )
    slug_category = AutoSlugField(
        populate_from='category_name',
    )

    def get_absolute_url(self):
        return reverse(
            'category', kwargs={'slug_category': self.slug_category}
        )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductImage(models.Model):
    image = models.ImageField(
        verbose_name='Фото',
        blank=True,
        upload_to='product/%Y/%m/%d/'
    )

    def get_absolute_url(self):
        return reverse('image_url', kwargs={'productimage_id': self.pk})

    def __str__(self):
        return str(self.image)


class ProductColor(models.Model):
    color = models.CharField(
        verbose_name='Цвет',
        max_length=255,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('color_url', kwargs={'productcolor_id': self.pk})

    def __str__(self):
        return self.color


class FavoriteUserProduct(models.Model):
    product_in_favorite = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='Продукт добаленный в избранное',
    )
    favorite_product_user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE,
        verbose_name='Пользователь добавивший в избранное'
    )

    def __str__(self):
        return f'{self.favorite_product_user}: {self.product_in_favorite}'

    class Meta:
        verbose_name = 'Favorites product'
        verbose_name_plural = 'Favorites products'
