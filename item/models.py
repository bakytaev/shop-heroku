from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=127)
    price = models.FloatField()

    def __str__(self):
        return self.title
