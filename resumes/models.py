from django.db import models
from django.contrib.auth import get_user_model


class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Rather Not Say'),
    )
    user = models.ForeignKey()
    title = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    is_married = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}: {self.title}'
