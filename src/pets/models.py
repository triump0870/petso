from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
PET_TYPE_CHOICE = (
    ('dog', 'Dog'),
    ('cat', 'Cat')
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_day = models.DateField(blank=False, null=False)
    owner = models.ForeignKey(User)
    type = models.CharField(max_length=3, choices=PET_TYPE_CHOICE, blank=False, null=False)

    def __str__(self):
        return self.name