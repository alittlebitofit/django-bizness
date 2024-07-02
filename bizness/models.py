from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.title}"

    @property
    def get_description(self):
        res = ""
        all_descriptions = self.descriptions.all()
        for (ind, ele) in enumerate(all_descriptions):
            res = res + ele.description
            if ind < len(all_descriptions)-1:
                res += ", "

        return res






class CardDescription(models.Model):
    card = models.ForeignKey(Card, related_name='descriptions', on_delete=models.CASCADE)
    description = models.TextField()







class Subscription(models.Model):
    first_name
    last_name
    mob_number
    email_id
    card
    message
