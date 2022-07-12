from django.db import models

# Create your models here.
class ShoppingItem(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveBigIntegerField()
    checked = models.BooleanField(default=False)
    added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-added']

# class Profile(models.Model):
#     user =models.OneToOneField('User')