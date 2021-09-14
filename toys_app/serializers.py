from rest_framework import serializers
from toys_app.models import ToysList


class ToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToysList
        fields = ('id',
                  'created',
                  'name',
                  'description',
                  'toy_category',
                  'release_date')