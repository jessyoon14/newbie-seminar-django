from django.db import models


# Create your models here.
class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['created']
