from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name