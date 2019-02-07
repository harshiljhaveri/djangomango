from django.conf import settings
from django.db import models
from django.utils import timezone

class mailing(models.Model):
    email =  models.EmailField(max_length=254)
    