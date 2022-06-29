from .models import Cart
from django.db.models.signals import (
    m2m_changed,
)
from django.dispatch import receiver

from .services.basket_calculator import BasketCalculator


@receiver(m2m_changed, sender=Cart.products.through)
def cart_m2m_changed_save_signal(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        basket_calculator = BasketCalculator()
        basket_calculator.basket_calculation(instance)
        instance.save()
