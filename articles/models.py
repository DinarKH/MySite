from django.db import models

class Articles(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    status=models.IntegerField()
    winner=models.IntegerField()
    objects = models.Manager()

class Bat(models.Model):
    user=models.IntegerField()
    #lot=models.ForeignKey(Articles)
    bat_date=models.DateTimeField()
    amount=models.IntegerField()



