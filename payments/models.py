from django.db import models
from django.contrib.auth import get_user_model


AuthUserModel = get_user_model()

class StripeCustomer(models.Model):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='stripe_customer')
    stripe_id = models.CharField(max_length=55, default=None, null=True)


class StripeCard(models.Model):
    stripe_customer = models.ForeignKey(StripeCustomer, on_delete=models.CASCADE, related_name='cards')
    stripe_id = models.CharField(max_length=255, default=None, null=True)
