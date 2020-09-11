from django.db import models
from payment.settings import BASE_URL, BITLY_API_KEY, BITLY_GROUP, BITLY_BASE_URL
import requests
import json


class Payment(models.Model):
    """
    Payment Informations
    """
    invoice_number = models.CharField(max_length=10, unique=True)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=254, unique=True)
    project_name = models.CharField(max_length=100)
    amount = models.IntegerField(null=False, blank=False)
    short_url = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)
        payment = Payment.objects.latest('id')
        if payment.short_url == '' or payment.short_url is None:
            long_url = BASE_URL + 'api/p1/payment/' + str(self.id) + '/'
            payment.short_url = self.set_shortlink(long_url)
            payment.save()

    def set_shortlink(self, long_url):
        headers = {
            "Authorization": "Bearer " + BITLY_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
            "group_guid": BITLY_GROUP,
            "domain": "bit.ly",
            "long_url": long_url
        }
        url = BITLY_BASE_URL
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            content = json.loads(response.content)
            return content['link']

    def __str__(self):
        return '%s %s %s' % (self.id, self.client_name, self.client_email)
