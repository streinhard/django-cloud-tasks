from testapp import models
from django_cloud_tasks import task

@task(queue='default')
def increment(request=None):
    counter, _ = models.Counter.objects.get_or_create(pk=1)
    counter.count += 1
    counter.save()