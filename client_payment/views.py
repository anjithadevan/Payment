from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import stripe
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

from client_payment.models import Payment
from client_payment.serializers import PaymentSerializer


class PaymentViewSet(APIView):
    queryset = Payment.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                payment = Payment.objects.get(id=serializer.data['id'])
                customer = stripe.Customer.create(email=payment.client_email, name=payment.client_name,
                                                  source=serializer.data['stripeToken'])
                charge = stripe.Charge.create(customer=customer, amount=payment.amount, currency="inr")
                payment.payment_status = True
                payment.save()
                return Response('success', status=HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response('Failed', status=HTTP_400_BAD_REQUEST)
        return Response('Failed', status=HTTP_400_BAD_REQUEST)
