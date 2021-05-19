from django.shortcuts import render, redirect
from . import models

def index(request):
    if(not request.user.is_authenticated):
        return redirect("/")

    context = {
        "campaigns": models.Campaign.objects.filter(creator=request.user)
    }
    return render(request, "dashboard/index.html", context)