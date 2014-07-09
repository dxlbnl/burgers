from django.shortcuts import render
from django.http import HttpResponse

from client.models import Burger, Order

import json
# Create your views here.


def index(request):
	context = {
	}

	return render(request, "order.html", context)


def order(request):

	if request.POST:
		# Create the order
		burgers = json.loads(request.POST['burgers'])
		address = json.loads(request.POST['address'])

		# Just let it run, and catch failures. (Validation ?)
		order = Order(**address)
		

		for burger in burgers:
			# Just let it run, and catch failures.
			burger_model = Burger(order=order, **burger)

			burger_model.save()





	return HttpResponse(json.dumps({
		'burgers' : burgers,
		'address' : address
	}),mimetype='application/json')