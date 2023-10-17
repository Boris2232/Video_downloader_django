from django.db import models


class People(models.Model):
    name = models.CharField(max_length=25, blank=False)
    password = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.name
