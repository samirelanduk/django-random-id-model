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

By default the ID will be 15 digits long, but you can override this in
settings.py with the `ID_DIGITS_LENGTH` setting.

`RandomIDModel` inherits directly from `models.Model` and does not interfere
with anything else, so you can use it wherever you would use `models.Model`. 
