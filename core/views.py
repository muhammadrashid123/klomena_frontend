from django.shortcuts import render


# Create your views here.
def home(request):
    print("nhhjj")
    return render(request, 'core/home.html')
