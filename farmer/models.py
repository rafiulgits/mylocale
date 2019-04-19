from account.models import Account

from django.db import models

from uuid import uuid4

from generic.variables import CROP_IMAGE_DIR


FOOD_CATEGORY = (
	('Rc', 'Rice'),
	('Fr', 'Fruits'),
	('Vg', 'Vegetables'),
	('Ot', 'Others')
)

FOOD_CATEGORY_DIC ={
	'Rc' : 'Rice',
	'Fr' : 'Fruits',
	'Vg' : 'Vegetables',
	'Ot' : 'Others'
}


class Crop(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	category = models.CharField(max_length=2, choices=FOOD_CATEGORY, default='Ot')
	name = models.CharField(max_length=80)
	description = models.TextField()
	media = models.ImageField(upload_to=CROP_IMAGE_DIR)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)




class Event(models.Model):
	uid = models.UUIDField(default=uuid4, primary_key=True)
	title = models.CharField(max_length=80)
	description = models.TextField()
	time = models.TimeField()
	date = models.DateField()
	address = models.CharField(max_length=50)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)