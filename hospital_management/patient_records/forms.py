from django.db import models
from django.db.models import fields
from django import forms
from django.forms import ModelForm
from .models import SELECT_GENDER, Person
from django_countries.data import COUNTRIES
from django_countries.fields import CountryField


class PatientForm(forms.ModelForm):
    class Meta:

        model = Person
        fields = [
            'first_name', 
            'middle_name', 
            'last_name', 
            'date_of_birth', 
            'gender', 
            'nationality',
            'address',
            # 'created_on',
            # 'created_by',
        ]


    def get_date(self):
        self.date_of_birth = forms.CharField(max_length=10, widget=forms.DateInput)
