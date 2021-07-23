from django.db import models

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length = 255)
    rating = models.IntegerField(choices =  [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])

    def __str__(self):
        return f"{self.quote} - {self.author}"