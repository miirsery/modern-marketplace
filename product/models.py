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
        validators=[MinValueValidator(1), MaxValueValidator(2147483647)]
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
        verbose_name='Количество товара',
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'product_detail', kwargs={'product_detail_slug': self.slug}
        )

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
