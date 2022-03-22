from django.db import models
# from numpy import true_divide
class signup(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=80)
    phno=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    uname=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)





# Create your models here.
