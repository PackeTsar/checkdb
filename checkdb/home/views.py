from django.shortcuts import render
from .models import Record


def index(request):
    return render(
        request,
        'homepage.html',
        {'records': Record.objects.all().order_by('-id')[:100]}
    )
