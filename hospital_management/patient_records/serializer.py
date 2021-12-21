from rest_framework import serializers, fields
import datetime

from .models import Person

class PersonOrPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person

        fields = [
            # 'id', 
            'first_name', 
            'middle_name', 
            'last_name', 
            'date_of_birth', 
            'gender', 
            'nationality',
            'address',
            'created_on',
            'created_by',
]