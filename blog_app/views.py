from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def home(request, template_name='blog/index.html'):
    return render(request, template_name)
