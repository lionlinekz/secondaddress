from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class SubscriptionType(models.Model):
	name = models.CharField(max_length=128)
	days = models.IntegerField(default = 0)
	monthly_fee = models.FloatField(default = 0)
	notification = models.BooleanField(default=False)
	amount_of_addresses = models.IntegerField(default = 0)
	amount_of_shipments = models.IntegerField(default = 0)
	number_of_persons_empowered = models.IntegerField(default = 0)
	store_shipment_fee = models.FloatField(default = 0)

	def __unicode__(self):
		return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User)
    level = models.ForeignKey(SubscriptionType)
    available_shipments = models.IntegerField(default=0)
    extra_shipments = models.IntegerField(default = 0)
    first_addressee_name = models.CharField(max_length=128, default="")
    second_addressee_name = models.CharField(max_length=128, default="")
    first_addressee_phone = models.CharField(max_length=64, default="")
    second_addressee_phone = models.CharField(max_length=64, default="")
    saver = models.BooleanField(default=False)
    renew_date = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.user.username

class PersonEmpowered(models.Model):
	subscription = models.ForeignKey(Subscription)
	name = models.CharField(max_length=128)
	surname = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)

	def __unicode__(self):
		return self.surname

class Day(models.Model):
	opening = models.TimeField(blank=True)
	close = models.TimeField(blank=True)
	break_start = models.TimeField(blank=True)
	break_close = models.TimeField(blank=True)
	opening_weekend = models.TimeField(blank=True)
	close_weekend = models.TimeField(blank=True)
	break_start_weekend = models.TimeField(blank=True)
	break_close_weekend = models.TimeField(blank=True)

	def __unicode__(self):
		return str(self.opening)


class Shopkeeper(models.Model):
	user = models.OneToOneField(User)
	tax_code = models.CharField(max_length=128)
	shop_name = models.CharField(max_length=512)
	shop_street = models.CharField(max_length=512)
	postal_code = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	region = models.CharField(max_length=128)
	phone = models.CharField(max_length=128)
	mobile_phone = models.CharField(max_length=128)
	timetable = models.ForeignKey(Day)

	def __unicode__(self):
		return self.user.username

class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=128)

    def __str__(self):  
          return "%s's profile" % self.user 

class Address(models.Model):
	subscription = models.ForeignKey(Subscription)
	shopkeeper = models.ForeignKey(Shopkeeper)

	def __unicode__(self):
		return self.shopkeeper.shop_name