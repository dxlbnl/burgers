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
    def get_options(cls):
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
        # Build the options object

        db_options = cls.objects.all()
        options = []
        for key, group in groupby(cls.objects.all(), lambda opt: opt.name):

            group = list(group)

            if len(group) > 1:
                options.append({
                    "name": key,
                    "values" : [{
                        'value': opt.value,
                        'price': float(opt.price),
                        'default': opt.default
                    } for opt in group]
                })
            else:
                options.append({
                    "name": key,
                    'price': float(group[0].price),
                    'default': group[0].default
                })

        # # Group by name
        # for db_opt in db_options:
        #     if db_opt.name in options:
        #         options[db_opt.name].append({
        #             'value': db_opt.value,    
        #             'price': float(db_opt.price),    
        #             'default': db_opt.default,    
        #         })
        #     elif db_opt.value:
        #         options[db_opt.name] = [{
        #             'value': db_opt.value,
        #             'price': float(db_opt.price),
        #             'default': db_opt.default,
        #         }]    
        #     else:
        #         options[db_opt.name] = {
        #             'name': db_opt.name,
        #             'price': float(db_opt.price),
        #             'default': db_opt.default,
        #         }

        return options

    @classmethod 
    def set_options(cls, options):
        """Flattens options, and stores the options"""

        # Just remove everything and write everything, bit ugly ;)
        cls.objects.all().delete()


        for option in options:

            if 'values' in option:
                for value in option['values']:
                    Ingredient(name=option['name'], **value).save()
            else:
                Ingredient(**option).save()


    def __unicode__(self):
        return "Ingredient {}:{}".format(self.name, self.value)


class Order(models.Model):

    name = models.CharField(max_length=20)

    # Address
    street = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    postal = models.CharField(max_length=8)

    time_ordered = models.TimeField(auto_now_add=True)

    # Status info
    ORDERED = "O"
    IN_PROGRESS = "P"
    ON_THE_ROAD = "R"
    DELIVERED = "D"

    status = models.CharField(max_length=1, choices=(
        (ORDERED, "Ordered"),
        (IN_PROGRESS, "In progress"),
        (ON_THE_ROAD, "On the road"),
        (DELIVERED, "Delivered")
    ), default=ORDERED)


    def get_absolute_url(self):
        return "/order/{}/".format(self.id)


class Burger(models.Model):
    """The Burger """

    ingredients = models.ManyToManyField(Ingredient, through='BurgerContents')

    # Order 
    order = models.ForeignKey('Order', related_name='burgers')


class BurgerContents(models.Model):
    
    burger = models.ForeignKey(Burger)
    ingredient = models.ForeignKey(Ingredient)
