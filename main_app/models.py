from django.db import models

from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

class Beer(models.Model):
    brewery= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    profile=models.CharField(max_length=50)
    abv= models.IntegerField()
    location = models.CharField(max_length=50)



    
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feed')

class Photo(models.Model):
    url = models.CharField(max_length=100)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for beer_id: {self.beer_id} @{self.url}"