from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    spent = models.BooleanField(default=True)
