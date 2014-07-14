from django.http import HttpResponse
from django.core import serializers
from django.utils.timesince import timesince
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, decorators


from client.models import Burger, Order, Ingredient, BurgerContents

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

        import pprint
        pprint.pprint(burgers)

        # Just let it run, and catch failures. (Validation ?)
        order = Order(**address)
        order.save()
        

        for burger in burgers:
            # Just let it run, and catch failures.
            burger_model = Burger(order=order)
            burger_model.save()

            for ingredient, value in burger.iteritems():
                # Add all ingredients to the burger.
                print ingredient, value
                if value:
                    ing_model = Ingredient.objects.filter(name=ingredient)
                    if (ing_model.count() > 1):
                        ing_model = ing_model.get(value=value)
                    elif ing_model.count() == 1:
                        ing_model = ing_model[0]
                    else:
                        raise ValueError("Invalid option '{}'".format(ingredient))
                    BurgerContents(burger=burger_model, ingredient=ing_model).save()

            burger_model.save()


        return redirect('/')

    elif order_id:
        return HttpResponse(json.dumps({
            'burgers' : burgers,
            'address' : address
        }),mimetype='application/json')

    else:
        return redirect('/')

@decorators.login_required
def orders(request):
    return render(request, "orders.html")

@decorators.login_required
def order_list(request):


    if request.method == "POST":
        req =  json.loads(request.body)

        if 'update' in req:
            order = Order.objects.get(id=req['update'])
            for key, value in req['data'].iteritems():
                setattr(order, key, value)

            order.save()


        return HttpResponse(json.dumps([]),mimetype='application/json')

    else:

        # Get the parameters
        limit = ('limit' in request.GET) and request.GET['limit'] or 20
        start = ('start' in request.GET) and request.GET['start'] or 0

        # Build the orders response
        # Should check if django uses joins like this.
        orders = [{
            'id': order.id,
            'status': order.get_status_display(),
            'name': order.name,
            'street': order.street,
            'place': order.place,
            'postal': order.postal,
            'time_ordered': timesince(order.time_ordered),

            "burgers": [{
                    ingredient.name: {
                        'value' : ingredient.value,
                        'price' : float(ingredient.price)
                    } for ingredient in burger.ingredients.all()
                } for burger in order.burgers.all()
            ]
        } for order in Order.objects.all()[start:start+limit] ]

        return HttpResponse(json.dumps(orders),mimetype='application/json')



@decorators.login_required
def ingredients(request):
    """Returns the burger options, ingredients, pricing enz."""


    if request.method == "POST":
        ingredients = json.loads(request.POST['ingredients'])

        Ingredient.set_all(ingredients)
        return redirect("/ingredients")


    # Respond to a normal call
    return render(request, "ingredients.html")


@decorators.login_required
def ingredients_list(request):

    # Respond to a ajax call
    ingredients = Ingredient.get_all()

    return HttpResponse(json.dumps(ingredients),mimetype='application/json')


@decorators.login_required
def logout_view(request):

    logout(request)
    # Redirect to a success page.

    return index(request)

def login_view(request):
    if request.POST:

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                pass
        else:
            pass
            # Return an 'invalid login' error message.

        if 'next' in request.GET:
            return redirect(request.GET['next'])
        return index(request)
    else:
        return render(request, "login.html")