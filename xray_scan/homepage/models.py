from django.db import models

# Create your models here.
class Upload_img(models.Model):
    img=models.ImageField(upload_to='homepage/static/homepage/image/')

    def __str__(self):
        return str(self.id)