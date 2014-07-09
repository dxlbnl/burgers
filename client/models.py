from django.db import models


# A Fieldtype to store lists, decrease database complexity.
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)







class IngredientType(models.Model):
	"""IngredientType"""

	name = models.CharField(max_length=20)
	options = ListField()


class Ingredient(models.Model):

	type = models.ForeignKey(IngredientType)
	value = models.CharField(max_length=80)



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

	ingredients = models.ManyToManyField(Ingredient)

	# Ingredients
	NO_CHEESE = "NC"
	CHEESE = "C"
	DOUBLE_CHEESE = "DC"

	RARE = "R"
	MEDIUM = "M"
	WELL_DONE = "W"

	cheese = models.CharField(max_length=2, choices=(
		(NO_CHEESE, "No cheese"),
		(CHEESE, "cheese"),
		(DOUBLE_CHEESE, "Double cheese")
	), default=CHEESE)
	meat = models.CharField(max_length=1, choices=(
		(RARE, "Rare"),
		(MEDIUM, "Medium"),
		(WELL_DONE, "Well done")
	), default=MEDIUM)

	bacon = models.BooleanField(default=False)
	tomatoes = models.BooleanField(default=False)
	cucumber = models.BooleanField(default=False)
	cabbage = models.BooleanField(default=False)

	# Order 
	order = models.ForeignKey('Order')
