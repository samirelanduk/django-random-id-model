# Django Random ID Model

This module provides a base class for Django models that gives them a random
primary key id.

For example, this is the vanilla way to do primary keys:

```python
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)

customer1 = Customer.objects.create(name="John")
customer2 = Customer.objects.create(name="Jane")
print(customer1.id) # '1'
print(customer2.id) # '2'
```

The primary key just auto increments.

Now use `RandomIDModel`:

```python
from django.db import models
from django_random_id_model import RandomIDModel

class Customer(RandomIDModel):
    name = models.CharField(max_length=50)

customer1 = Customer.objects.create(name="John")
customer2 = Customer.objects.create(name="Jane")
print(customer1.id) # '725393588906066'
print(customer2.id) # '905529381860540'
```

The ID is guaranteed to be unique.

By default the ID will be 12 digits long, but you can override this in
settings.py with the `ID_DIGITS_LENGTH` setting.

`RandomIDModel` inherits directly from `models.Model` and does not interfere
with anything else, so you can use it wherever you would use `models.Model`.

## Forms and Admin

To integrate your model with a Django ModelForm, you will need to manually
exclude the `id` field:

```python
from django.forms import ModelForm

class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        exclude = ["id"]
```

Likewise if you use the Django Admin app:

```python
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    exclude = ["id"]

admin.site.register(Customer, CustomerAdmin)
```
