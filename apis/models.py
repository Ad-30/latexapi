from django.db import models
 
 
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
 
    def __str__(self):
        return self.title
    
from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)