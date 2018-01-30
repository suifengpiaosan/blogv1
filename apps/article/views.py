from django.shortcuts import render
from article.models import Articles
# Create your views here.

def home(request):
    if request.method == "GET":
        all_Articles = Articles.objects.all()
        if all_Articles:
                return render(request,'home.html',{"Article":all_Articles})