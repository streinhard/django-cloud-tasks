from django.shortcuts import render

from testapp import models, tasks

def counter(request):
    tasks.increment()
    counter = models.Counter.objects.get(pk=1)
    return render(request, 'counter.html', {
        'counter': counter.count
    })