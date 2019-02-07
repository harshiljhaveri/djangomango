from django.conf import settings
from django.db import models
from django.utils import timezone

class Posts(models.Model):
    name = models.CharField(max_length=200)
    texts = models.TextField(default='Enter your feedback here')
    email =  models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    
def __str__(self):
    return self.texts