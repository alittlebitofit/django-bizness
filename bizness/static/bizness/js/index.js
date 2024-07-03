// alert("TEST");

document.getElementById('subscriptionForm').addEventListener('submit', function(event) {
	event.preventDefault();  // Prevent default form submission
	let form = event.target;
	let formData = new FormData(form);

	fetch(form.action, {
		method: 'POST',
		body: formData,
		headers: {
			'X-Requested-With': 'XMLHttpRequest'  // To signal this is an AJAX request
		}
	})

	.then(response => {
		const contentType = response.headers.get('Content-Type');
		if (!response.ok) {

			// document.querySelector("input[name='csrfmiddlewaretoken']")

			if (contentType && contentType.includes('application/json')) {
				return response.json().then(errorData => {
					throw new Error(errorData.message || 'Unknown error');
				});
			} else {
				return response.text().then(errorText => {
					throw new Error(errorText || 'Unknown error');
				});
			}
		}
		if (contentType && contentType.includes('application/json')) {
			return response.json();
		} else {
			return response.text();
		}
	})

	.then(data => {
		console.log('Success:', data);  // Handle the JSON response here
	})
	.catch((error) => {
		console.error('Error:', error);
	});
});