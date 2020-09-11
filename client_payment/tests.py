from rest_framework import status
from rest_framework.test import APITestCase

from client_payment.models import Payment


class TestPaymentViewSet(APITestCase):
    def test_post(self):
        payment = Payment.objects.create(invoice_number='test1', client_name='test', client_email='test@gmail.com',
                                         amount=1000)
        url = '/api/p1/payments'
        data = dict()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'stripeToken': '', 'id': payment.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
