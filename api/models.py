from django.db import models
import datetime
class User(models.Model):
    name = models.TextField()
    author = models.TextField()
    img = models.ImageField(upload_to='img/')
    audio = models.FileField(upload_to='audio/')
    add_date= models.DateTimeField( auto_now_add=True)
    lyrics = models.TextField()
    
    
    
    
    
