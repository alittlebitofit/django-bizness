from django.forms import ModelForm
from django import forms

from bizness.models import Card, Subscription


class CardRadioSelect(forms.RadioSelect):
    template_name = 'bizness/widgets/card_radio_select.html'


class SubscriptionModelForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ["first_name", "last_name", "phone_number", "email", "card", "message"]
        widgets = {
            'card': forms.RadioSelect(attrs={'class': 'radio-select'}),
            'message': forms.Textarea(attrs={'placeholder': "If there's anything else you would like us to know..."})
        }

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None)
    #     super().__init__(*args, **kwargs)
    #     if user:
    #         self.fields['card'].queryset = Card.objects.all()
