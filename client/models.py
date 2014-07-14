from django.db import models

from itertools import groupby

class Ingredient(models.Model):

    """An Ingredient has a name and value, to store all the possible different options of a burger. """

    name = models.CharField(max_length=20, blank=False)
    value = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    default = models.NullBooleanField()

    unique_together = (('name', 'value'))


    @classmethod
    def get_all(cls):
        """
            Creates an object which represents all the options in the database.
            returns [
                {
                    name: str,
                    default: bool,
                    price: float,
                }, 
                or 
                {
                    name: str,
                    values: [*{
                        value: str,
                        price: float,
                        default: bool
                    }]
                }
            ]
        """
        # Build the ingredients object

        ingredients = []
        for key, group in groupby(cls.objects.all(), lambda opt: opt.name):

            group = list(group)

            if len(group) > 1:
                ingredients.append({
                    "name": key,
                    "values" : [{
                        "id": opt.id,
                        'value': opt.value,
                        'price': float(opt.price),
                        'default': opt.default
                    } for opt in group]
                })
            else:
                ingredients.append({
                    "id": group[0].id,
                    "name": key,
                    'price': float(group[0].price),
                    'default': group[0].default
                })

        return ingredients

    @classmethod 
    def set_all(cls, ingredients):
        """Flattens ingredients, and stores the ingredients"""

        # A set of not updated id's
        not_updated = {ingredient['id'] for ingredient in Ingredient.objects.all().values('id')}

        for option in ingredients:

            if 'values' in option:
                for value in option['values']:
                    if 'id' in value:
                        ing = cls.objects.get(id=value['id'])

                        # Update
                        ing.name = option['name']
                        ing.value = value['value']
                        ing.price = value['price']
                        ing.default = (option['default'] == ing.value)

                        not_updated.remove(ing.id)
                    else:
                        # create it
                        ing = cls(name=option['name'], **value)

                    ing.save()
            else:
                if 'id' in option:
                    ing = cls.objects.get(id=option['id'])

                    # Update
                    ing.name = option['name']
                    ing.price = option['price']
                    ing.default = option['default']

                    not_updated.remove(ing.id)
                else:
                    # create it
                    ing = cls(**option)

                ing.save()

        # remove the not updated ingredients.
        if not_updated:
            not_updated = cls.objects.filter(reduce(lambda x, y: x | y, [models.Q(id=id) for id in not_updated]))
            not_updated.delete()




    def __unicode__(self):
        return "Ingredient {}:{}".format(self.name, self.value)


class Order(models.Model):

    name = models.CharField(max_length=20)

    # Address
    street = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    postal = models.CharField(max_length=8)

    time_ordered = models.DateTimeField(auto_now_add=True)

    # Status info
    ORDERED = "O"
    IN_PROGRESS = "P"
    ON_THE_ROAD = "R"
    DELIVERED = "D"
    
    STATUS_OPTS = (
        (ORDERED, "Ordered"),
        (IN_PROGRESS, "In progress"),
        (ON_THE_ROAD, "On the road"),
        (DELIVERED, "Delivered")
    )



    status = models.CharField(max_length=1, choices=STATUS_OPTS, default=ORDERED)

    def __str__(self):
        return "Order for {}".format(self.name)

    def get_absolute_url(self):
        return "/order/{}/".format(self.id)


class Burger(models.Model):
    """The Burger """

    ingredients = models.ManyToManyField(Ingredient, through='BurgerContents')

    # Order 
    order = models.ForeignKey('Order', related_name='burgers')

    def __str__(self):
        return "Burger in {}".format(self.order)

class BurgerContents(models.Model):
    
    burger = models.ForeignKey(Burger)
    ingredient = models.ForeignKey(Ingredient)
