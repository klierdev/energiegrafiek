from rest_framework import serializers
from Data.models import EnergieTerug

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EnergieTerug 
        fields = "__all__"