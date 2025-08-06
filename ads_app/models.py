from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    CONDITION_CHOICES = [('new', 'New'), ('used', 'Used')]
    Catigory_CHOICES = [('electronics', 'Electronics'), ('furniture', 'Furniture'), ('clothing', 'Clothing')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=Catigory_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

class ExchangeProposal(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]

    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='sent_offers')
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='received_offers')
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

