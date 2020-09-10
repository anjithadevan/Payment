from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

import stripe
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.response import Response

from client_payment.models import Payment


class PaymentViewSet(APIView):
    queryset = Payment.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        if request.data['stripeToken']:
            try:
                payment = Payment.objects.get(id=request.data['id'])
                customer = stripe.Customer.create(email=payment.client_email, name=payment.client_name, source=request.data['stripeToken'])
                charge = stripe.Charge.create(customer=customer, amount=payment.amount, currency="inr")
                payment.payment_status = True
                payment.save()
                return Response('success', status=HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response('Failed', status=HTTP_400_BAD_REQUEST)
        return Response('Failed', status=HTTP_400_BAD_REQUEST)


