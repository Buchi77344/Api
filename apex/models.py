from django.db import models

# Create your models here.


class Notepad(models.Model):
    title = models.CharField( max_length=120,)
    note =models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
