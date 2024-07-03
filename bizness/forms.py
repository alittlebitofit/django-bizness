from django.forms import ModelForm

from bizness.models import Subscription

class SubscriptionModelForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ["first_name", "last_name", "phone_number", "email", "card", "message"]