from django.db import models


class Pet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=20, choices=PET_TYPES)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(default=0)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name