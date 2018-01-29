from django.shortcuts import render
from article.models import Articles
# Create your views here.

def home(request):
    if request.method == "GET":
        all_Articles = Articles.objects.all()
        if all_Articles:
            for Article in all_Articles:
                title = Article.title
                body = Article.body
                # author = Article.author
                return render(request,'home.html',{'title':title,
                                                   'body': body})