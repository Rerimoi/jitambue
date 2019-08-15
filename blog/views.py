from django.shortcuts import render,redirect
from django.views import View
from .models import Category, Article

# Create your views here.
def home(request):
    return render(request, 'blog/base.html', {})

class Articles(View):
    template = 'articles.html'

    def get(self, request, category_id):
        category =Category.objects.get(id=category_id)
        articles = Article.objects.filter(Category=category)
        return render(request, self.template, {"articles":articles})

class Article_detail(View):
    template ='articleDetails.html'

    def get(self,request,article_id):
        article= Article.objects.get(id=article_id)
        return render(request,self.template,{"article":article})


class contents(View):
    template = 'knowzone.html'

    def get(self,request):
        categories = Category.objects.all()
        print(categories)
        return render(request, self.template,{'categories':categories})
