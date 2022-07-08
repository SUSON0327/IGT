from django.db import models

# class Haveyour_say(models.Model):
# 	YourName=models.TextField(blank = True)
# 	YourEmail=models.TextField(blank = True)
# 	YourExperience=models.TextField(blank = True)
class Items(models.Model):
	Product = models.CharField(blank = True, max_length = 100)
	QuaPrice = models.CharField(blank = True, max_length = 100)
	Sizes = models.CharField(blank = True, max_length = 50)

class ProfileInfo(models.Model):
	First_name = models.CharField(blank = True, max_length = 100)
	Last_name = models.CharField(blank = True, max_length = 100)
	Email = models.CharField(blank = True, max_length = 100)
	Address = models.CharField(blank = True, max_length = 250)
	Contact_number = models.CharField(blank = True, max_length = 250)
	Notes = models.CharField(blank = True, max_length = 300)

class Payment(models.Model):
	TDate = models.CharField(blank = True, max_length = 100)
	DDate = models.CharField(blank = True, max_length = 100)
	Pay = models.CharField(blank = True, max_length = 100)


