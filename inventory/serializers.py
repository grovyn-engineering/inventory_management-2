from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    class Meta:
       model = Product
       fields = "__all__"
