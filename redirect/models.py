from django.db import models
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from django.core.cache import cache
from .exceptions import RedirectKeyNotExist


class Redirect(models.Model):
    key = models.CharField('Key', max_length=50)
    url = models.URLField('Url', max_length=200)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,
                                      db_index=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True,
                                      db_index=True)

    def __str__(self):
        return self.url

    @classmethod
    def get_redirect(cls, key):
        if not cache.get(key):
            raise RedirectKeyNotExist("La clave no existe o no esta activa.")
        return cache.get(key)


def add_key_cache(sender, instance, **kwargs):
    if instance.active:
        cache.set(instance.key, model_to_dict(instance))
    else:
        cache.delete(instance.key)


post_save.connect(add_key_cache, sender=Redirect)
