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



from django.core.validators import RegexValidator

class Subscription(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '+919876543210'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list

    email = models.EmailField(max_length=254, blank=True)
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    message = models.TextField(default='', blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
