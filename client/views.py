from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from client.models import Burger, Order, Ingredient

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


def orders(request):

    return index(request)

def options(request):
    """Returns the burger options, ingredients, pricing enz."""

    return render(request, "options.html")

def option_values(request):

    if request.method == "POST":
        options = json.loads(request.POST['options'])

        for option in options: 
            # Get the stored values.

            for value in option['values']:
                Ingredient(name=option['name'], **value).save()


        print options
        return redirect("/options")


    else:
        options = Ingredient.get_options()

    return HttpResponse(json.dumps(options),mimetype='application/json')


def logout_view(request):

    logout(request)
    # Redirect to a success page.

    return index(request)

def login_view(request):
    if request.POST:

        username = request.POST['username']
        password = request.POST['password']
        print "Checking credentials", username
        user = authenticate(username=username, password=password)
        print "Found", user
        if user is not None:
            if user.is_active:
                print "Logging in"
                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                pass
        else:
            pass
            # Return an 'invalid login' error message.
        return index(request)
    else:
        return render(request, "login.html")