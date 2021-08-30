from django.db import models

class Counter(models.Model):

    count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return str(self.count)