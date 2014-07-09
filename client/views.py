from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from client.models import Burger, Order

import json
# Create your views here.


def index(request):
	return render(request, "order.html")


def order(request, order_id=None):
	"""Processes an order, or returns an existing one."""

	if request.POST:
		# Create the order
		burgers = json.loads(request.POST['burgers'])
		address = json.loads(request.POST['address'])

		# Just let it run, and catch failures. (Validation ?)
		order = Order(**address)
		order.save()
		

		for burger in burgers:
			# Just let it run, and catch failures.
			burger_model = Burger(order=order, **burger)

			burger_model.save()


		return redirect(order)

	elif order_id:
		return HttpResponse(json.dumps({
			'burgers' : burgers,
			'address' : address
		}),mimetype='application/json')

	else:
		return redirect('index')


def options(request):
	"""Returns the burger options, ingredients, pricing enz."""
	pass