from django.shortcuts import render

# Create your views here.
from bizness.models import Subscription, Card
from bizness.forms import SubscriptionModelForm


def index(request):
	"""View function for handling user subscription."""
	context = {}

	# If this is a POST request then process the Form data
	if request.method == 'POST':

		# Create a form instance and populate it with data from the request (binding):
		form = SubscriptionModelForm(request.POST)

		# Check if the form is valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required

            #TODO: need to store card data from form
			subscriber = Subscription(
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				phone_number = form.cleaned_data['phone_number'],
				email = form.cleaned_data['email'],
				card = form.cleaned_data['card'], #TODO: need to store card data from form
				message = form.cleaned_data['message'],
            )

			subscriber.save()

			#TODO: need to return JSONResponse as a success message
			return HttpResponseRedirect(reverse('borrowed'))

	# If this is GET (or any other method) create the default form.
	else:
		form = SubscriptionModelForm(
			initial = {
				'message': "If there's anything else you would like us to know..."
			}
		)

		#Since this is a GET request I need to pass all three card data to the user
		cards = Card.objects.all()
		context.update({
			'cards': cards,
		})


	context.update({
		'form': form,
	})

    #TODO: pass the valid template
	return render(request, 'catalog/book_renew_librarian.html', context)
