from django.shortcuts import render

from testapp import models, tasks

def counter(request):
    # Execute using Google Cloud Tasks
    #tasks.increment().execute()

    # Run locally
    tasks.increment().run()

    counter, _ = models.Counter.objects.get_or_create(pk=1)
    return render(request, 'counter.html', {
        'counter': counter.count
    })