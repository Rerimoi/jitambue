from django.shortcuts import render,redirect
from django.views import View
from .models import Category, Article, UserProfileInfo
from . import forms
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

class locateClinic(View):
    template = 'locateClinic.html'
    
    def get(self,request):
        return render(request,self.template, {})


class Signup(View):

    template = "registration/signup.html"
    form_class = forms.Signup

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name =last_name
        user.save()
        return redirect("login")

class Editprofile(View):
    form_class=forms.UserProfile
    template="userProfile.html"

    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template, {"form":form})

    def post(self,request):
        form=self.form_class(request.POST, request.FILES)
        username= request.user
        print(username, request.POST, request.FILES)
        # user=User.objects.get(username=username)
        # print(user)
        # profilePic= request.FILES["Profile_picture"]
        # sex= request.POST["sex"]
        # dateOfBirth= request.POST["Date_Of_birth"]
        # userProfile = UserProfileInfo.objects.create(profile_pic=profilePic, user=user, dateOfBirth=dateOfBirth,sex=sex)
        # userProfile.save() 
        return render(request, self.template, {"form":form})


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
