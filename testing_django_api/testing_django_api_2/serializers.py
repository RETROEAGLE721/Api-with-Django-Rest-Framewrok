from rest_framework import serializers
from.models import drinks

class django_api_2(serializers.ModelSerializer):
    class Meta:
        model = drinks 
        fields = '__all__'