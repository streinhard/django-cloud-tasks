from testapp import models


def increment():
    counter, _ = models.Counter.objects.get_or_create(pk=1)
    counter.count += 1
    counter.save()