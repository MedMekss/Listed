from . import models

def foo(request):
    context = {'categories': models.Category.objects.all()}

    return context
