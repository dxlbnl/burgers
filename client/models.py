from django.db import models

# Create your models here.


class Burger(models.Model):
	"""The burger model, created with some initial ingredients"""

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

	bacon = models.BooleanField(default=True)
	tomatoes = models.BooleanField(default=True)
	cucumber = models.BooleanField(default=True)
	cabbage = models.BooleanField(default=True)

	# Order 
	order = models.ForeignKey('Order')


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