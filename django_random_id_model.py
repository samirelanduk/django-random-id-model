from random import randint
from django.db import models
from django.conf import settings

__author__ = "Sam Ireland"
__version__ = "0.1.1"

def generate_random_id():
    try:
        digits = settings.ID_DIGITS_LENGTH
    except: digits = 12
    return randint(10 ** (digits - 1), 10 ** digits)


class RandomIDModel(models.Model):
    """Provides a custom ID primary key field - a random digit integer."""

    class Meta:
        abstract = True

    id = models.BigIntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        """If the user hasn't provided an ID, generate one at random and check
        that it has not been taken."""
        
        if not self.id:
            is_unique = False
            while not is_unique:
                id = generate_random_id()
                is_unique = not self.__class__.objects.filter(id=id).exists()
            self.id = id
        super(RandomIDModel, self).save(*args, **kwargs)