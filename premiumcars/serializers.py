from rest_framework.serializers import ModelSerializer

from premiumcars.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'price',
            'count',
        ]
