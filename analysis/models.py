from django.db import models


class NavItem(models.Model):
    name = models.CharField(max_length=255, default='')
    path = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.path

