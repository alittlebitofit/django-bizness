from django.shortcuts import render

# Create your views here.
from bizness.models import Subscription, Card
from bizness.forms import SubscriptionModelForm

from django.http import JsonResponse

def index(request):
	"""View function for handling user subscription."""

	print("ONE")
	# If this is a POST request then process the Form data
	if request.method == 'POST':
		print("TWO")

		# Create a form instance and populate it with data from the request (binding):
		form = SubscriptionModelForm(request.POST)

		# Check if the form is valid:
		if form.is_valid():
			
			print("THREE")
			# process the data in form.cleaned_data as required

			subscriber = Subscription(
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				phone_number = form.cleaned_data['phone_number'],
				email = form.cleaned_data['email'],
				card = form.cleaned_data['card'],
				message = form.cleaned_data['message'],
            )

			subscriber.save()
			print("fgdfgfgf")

			return JsonResponse(status=201)
		
		print(form.errors)

	# If this is GET (or any other method) create the default form and pass all the cards
	else:
		
		print("FOUR")
		cards = Card.objects.all()

		form = SubscriptionModelForm(
            initial = {
                'message': "If there's anything else you would like us to know..."
            }
        )
		
		form.fields['card'].queryset = cards


	context = {
		'form': form,
	}

	
	print("FIVE")

    #TODO: pass the valid template
	return render(request, 'bizness/index.html', context)
