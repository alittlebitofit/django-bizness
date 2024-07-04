from django.forms import ModelForm
from django import forms

from bizness.models import Subscription

class SubscriptionModelForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ["first_name", "last_name", "phone_number", "email", "card", "message"]
        widgets = {
            'card': forms.RadioSelect,
            'message': forms.Textarea(attrs={'placeholder': "If there's anything else you would like us to know..."})
        }