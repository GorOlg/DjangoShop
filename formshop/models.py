from django.db import models
# from django.utils import timezone


# Create your models here.


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biog = models.TextField()
    birthday = models.DateField()











"""
class Change(models.Model):
    time = models.DateTimeField(default=timezone.now)
    side = models.CharField(max_length=10)

    @staticmethod
    def values():
        value = Change.objects.order_by('-time')[:5]
        return value

    def __str__(self):
        return f'time: {self.time}, side: {self.side}'
"""


