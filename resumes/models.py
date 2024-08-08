from django.db import models
from django.contrib.auth import get_user_model


class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Rather Not Say'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    is_married = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.title}'


class ContactInfo(models.Model):
    resume = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Address = models.TextField()


class LanguageInfo(models.Model):
    Language_CHOICES = (
        (1, 'Too Low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'Good'),
        (5, 'Perfect'),
    )

    resume = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    level = models.CharField(choices=Language_CHOICES, max_length=1)


