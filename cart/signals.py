from .models import Cart
from django.db.models.signals import (
    post_save,
    pre_save,
)
from django.dispatch import receiver


@receiver(pre_save, sender=Cart)
def cart_pre_save_signal(sender, *args, **kwargs):
    print(f"pre_save - {kwargs} {args}")


@receiver(post_save, sender=Cart)
def cart_post_save_signal(sender, **kwargs):
    print(f"post_save - {kwargs} {sender}")
