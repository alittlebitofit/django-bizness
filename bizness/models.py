from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CardDescription(models.Model):
    card = models.ForeignKey(Card, related_name='descriptions', on_delete=models.CASCADE)
    description = models.TextField()
