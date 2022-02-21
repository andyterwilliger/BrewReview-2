from django.db import models

from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

class Beer(models.Model):




    user = models.ForeignKey(User, on_delete = models.CASCADE)
