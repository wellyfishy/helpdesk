from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

STATUS = (
    (1,'Diajukan'),
    (2,'Diproses'),
    (3,'Selesai')
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    status = models.IntegerField(choices=STATUS,default=1)
    foto_1 = models.ImageField(upload_to='POST/sebelum/', null=True)
    foto_2 = models.ImageField(upload_to='POST/sesudah/', blank=True, null=True)
    foto_default = models.ImageField(default='notfound.jpg', blank=True, null=True)
    teknisi = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='teknisi', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    


