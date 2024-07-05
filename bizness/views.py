from django.shortcuts import render

# Create your views here.
from bizness.models import Subscription, Card
from bizness.forms import SubscriptionModelForm

from django.http import JsonResponse

def index(request):
	"""View function for handling user subscription."""

	# If this is a POST request then process the Form data
	if request.method == 'POST':

		# Create a form instance and populate it with data from the request (binding):
		form = SubscriptionModelForm(request.POST)

		# Check if the form is valid:
		if form.is_valid():
			
			subscriber = Subscription(
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				phone_number = form.cleaned_data['phone_number'],
				email = form.cleaned_data['email'],
				card = form.cleaned_data['card'],
				message = form.cleaned_data['message'],
            )

			subscriber.save()

			form = SubscriptionModelForm()

			context = {
				'form': form,
			}

			return render(request, "bizness/index.html", context, status=201)
		
	# If this is GET (or any other method) create the default form and pass all the cards
	else:
		
		# cards = Card.objects.all()

		form = SubscriptionModelForm()
		
		# form.fields['card'].queryset = cards


	context = {
		'form': form,
	}

	return render(request, 'bizness/index.html', context)
