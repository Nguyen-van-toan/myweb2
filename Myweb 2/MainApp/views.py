from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
      return render(request, "pages/home.html")
def about(request):
      return render(request, "pages/about.html")
def explore(request):
      return render(request, "pages/explore.html")
def gallery(request):
      return render(request, "pages/gallery.html")
def contact(request):
      return render(request, "pages/contact.html") 
def login(request):
      return render(request, "pages/login.html") 


# Create your views here.
