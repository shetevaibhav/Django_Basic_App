from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello this is django app from producation and remove whitenoise!")