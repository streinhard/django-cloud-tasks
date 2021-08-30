from django.db import models

class Counter(models.Model):

    count = models.PositiveBigIntegerField(default=0)