from django.apps import AppConfig
from django.core.signals import request_finished


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'

    def ready(self):
        from . import signals
        request_finished.connect(
            signals.cart_pre_save_signal,
        )
        request_finished.connect(
            signals.cart_post_save_signal,
        )
