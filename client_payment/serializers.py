from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    stripeToken = serializers.CharField(max_length=200, required=True)
    id = serializers.IntegerField(required=True)
