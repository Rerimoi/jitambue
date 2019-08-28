from django.shortcuts import render,redirect
from django.views import View
from .models import Category, Article
from . import forms
from django.contrib.auth.models import User
# from .forms import ProfileForm
# from django.contrib.auth.decorators import login_required
# from django.db import transaction

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

class locateClinic(View):
    template = 'locateClinic.html'
    
    def get(self,request):
        return render(request,self.template, {})

class Login(View):
    template = "registration/login.html"
    
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
# user profile view
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
        
#         user_form = Signup(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('login')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = Signup(instance=request.user)
#         profile = Profile.objects.create(user=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'userProfile.html', {
#         'user_form': Signup,
#         'profile_form': ProfileForm

#         })

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
