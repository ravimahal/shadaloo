from rest_framework import serializers
from units.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        #choose what fields from the models we want to serialize
        fields = ('id', 'number', 'unit_name', 'image')