from locale import currency
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    address_Name = models.TextField()
    email_Address = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()

class Account(models.Model):
    account_number = models.CharField(max_length=20)
    account_name= models.CharField(max_length=30)
    balance = models.IntegerField()

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    date_created=models.DateTimeField()
    amount = models.IntegerField()   

class Transaction(models.Model):
    transaction_amount = models.IntegerField()
    date_time = models.DateTimeField()
    transaction_charge = models.IntegerField()
class Card(models.Model):
    cardholder_number = models.IntegerField()
    expiry_date = models.DateField()
    cardholder_name= models.CharField(max_length=30)
    
class ThirdParty(models.Model):
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    account = models.IntegerField()

class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField(max_length=40)
     wallet = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Wallet)

class Receipt(models.Model):
    transaction = models.IntegerField()
    receipt_date= models.DateTimeField()
    total_Amount= models.IntegerField()

class Loan(models.Model):
    wallet = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Wallet)
    interest_rate = models.IntegerField()
    loan_balance = models.IntegerField()

class Reward(models.Model):
    transaction = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Transaction)
    date_of_reward = models.DateTimeField()
    account = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Account)       


   


