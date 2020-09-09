from django.db import models


class Payment(models.Model):
    """
    Payment Informations
    """
    invoice_number = models.CharField(max_length=10)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=254)
    project_name = models.CharField(max_length=100)
    amount = models.IntegerField(null=False, blank=False)
    short_url = models.CharField(max_length=200)
    payment_status = models.BooleanField(default=False)