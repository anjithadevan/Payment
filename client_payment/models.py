from django.db import models
from django_bitly.models import Bittle
from django.conf import settings
from payment.settings import BASE_URL, BITLY_API_KEY
# import bitly_api


class Payment(models.Model):
    """
    Payment Informations
    """
    invoice_number = models.CharField(max_length=10, unique=True)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=254)
    project_name = models.CharField(max_length=100)
    amount = models.IntegerField(null=False, blank=False)
    short_url = models.CharField(max_length=200, blank=True)
    payment_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
        payment = Payment.objects.latest('id')
        if payment.short_url == '' or payment.short_url is None:
            bittle = Bittle.objects.bitlify(payment)
            payment.short_url = bittle.shortUrl
            payment.save()

    def get_absolute_url(self):
        path = BASE_URL + 'api/p1/payment/' + str(self.id) + '/'
        return path