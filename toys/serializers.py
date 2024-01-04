from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    # inner class used to specify metadata
    class Meta:
        fields = ("id", "purchaser", "title", "description", "created_at", "updated_at")
        model = Toy
