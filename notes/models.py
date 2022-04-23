from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


# Create your models here.
class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   default=None)

    class Meta:
        ordering = ['created']


