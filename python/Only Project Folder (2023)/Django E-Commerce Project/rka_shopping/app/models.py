from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models,models.CharField(max_length=200)
    locality = models,models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    STATE_CHOICES = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa','Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttarakhand','Uttarakhand'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
        ('Daman and Diu','Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep','Lakshadweep'),
        ('Puducherry', 'Puducherry'),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=50)


def __str__(self):
    return str(self.id)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    CATEGORY_CHOICE = (
        ('M', 'Mobile'),
        ('L', 'Laptop'),
        ('TW', 'Top Wear'),
        ('BW', 'Bottom Wear'),
    )
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50)
    Product_imgage = models.ImageField(upload_to='producting')


def __str__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models,models.PositiveIntegerField(default=1)


def __str__(self):
    return str(self.id)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models, models.PositiveIntegerField(default=1)
    ordered_date = models.DateField(auto_now_add=True)
    STATUS_CHOICE = (
        ('Accepted', 'Accepted'),
        ('Packed', 'Packed'),
        ('On The Way', 'On The Way'),
        ('Cancel', 'Cancel'),
    )
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')
