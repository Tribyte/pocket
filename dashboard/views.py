from django.shortcuts import render

def index(request):
    context = {}

    return render(context, "dashboard/index.html", request)