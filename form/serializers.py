from rest_framework import serializers
from .models import Myform

class Fromser(serializers.ModelSerializer):
    class Meta:
        model = Myform
        fields = ('id', 'name', 'email')
