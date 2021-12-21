from django.db import models
from django.forms import widgets
from django_countries.fields import CountryField
from django.conf import settings

SELECT_GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.CharField(max_length=1, choices=SELECT_GENDER)
    nationality = CountryField()
    address = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.first_name


    def get_user(self):
        if self.created_by == self.request.authenticated:
            self.created_by = True