from django.shortcuts import render

# Create your views here.
from bizness.models import Subscription
from bizness.forms import SubscriptionModelForm


def index(request):
	"""View function for renewing a specific BookInstance by librarian."""
	
    #TODO: i don't think I actually need this statement as it is not updating anything, its posting data, i.e. creating data for the first time.
	book_instance = get_object_or_404(BookInstance, pk=pk)

	# If this is a POST request then process the Form data
	if request.method == 'POST':

		# Create a form instance and populate it with data from the request (binding):
		form = SubscriptionModelForm(request.POST)

		# Check if the form is valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required (here we just write it to the model due_back field)
			
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
		#TODO: need to do something else if its a GET request
		#TODO: Maybe message should be optional, so change the model first and run migrations
		form = SubscriptionModelForm(
			initial = {
				'message': "If there's anything else you would like us to know..."
			}
		)

    #TODO: need to pass context for form errors or initial values
	context = {
		'form': form,
	}

    #TODO: pass the valid template
	return render(request, 'catalog/book_renew_librarian.html', context)