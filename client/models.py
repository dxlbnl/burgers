from django.db import models



class Ingredient(models.Model):

    """An Ingredient has a name and value, to store all the possible different options of a burger. """

    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    default = models.BooleanField(max_length=20)

    unique_together = (('name', 'value'))



class Order(models.Model):

    name = models.CharField(max_length=20)

    # Address
    street = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    postal = models.CharField(max_length=8)

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
    order = models.ForeignKey('Order')

    # # Ingredients
    # NO_CHEESE = "NC"
    # CHEESE = "C"
    # DOUBLE_CHEESE = "DC"

    # RARE = "R"
    # MEDIUM = "M"
    # WELL_DONE = "W"

    # cheese = models.CharField(max_length=2, choices=(
    #   (NO_CHEESE, "No cheese"),
    #   (CHEESE, "cheese"),
    #   (DOUBLE_CHEESE, "Double cheese")
    # ), default=CHEESE)
    # meat = models.CharField(max_length=1, choices=(
    #   (RARE, "Rare"),
    #   (MEDIUM, "Medium"),
    #   (WELL_DONE, "Well done")
    # ), default=MEDIUM)

    # bacon = models.BooleanField(default=False)
    # tomatoes = models.BooleanField(default=False)
    # cucumber = models.BooleanField(default=False)
    # cabbage = models.BooleanField(default=False)

class BurgerContents(models.Model):
    
    burger = models.ForeignKey(Burger)
    ingredient = models.ForeignKey(Ingredient)
