from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name= 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.Login.as_view(), name='login'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('knowzone/', views.contents.as_view(), name='knowzone'),
    path('knowzone/articles/<int:category_id>/', views.Articles.as_view(), name='articles'),
    path('knowzone/articles_details/<int:article_id>/', views.Article_detail.as_view(), name='article_detail'),
    path('locate_clinic/', views.locateClinic.as_view(), name='locate_clinic')
    
]