from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# User profile model

# class Profile(models.Model):
#     SEX_CHOICES= (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics',blank=True, null=True)
#     bio = models.TextField(max_length=500, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     sex = models.CharField( max_length= 10, choices = SEX_CHOICES)
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

    
    

# defines each category in SRH i.e GBV,Abortion, Hygiene
class Category(models.Model):
    image=models.ImageField()
    name= models.CharField(max_length=200)
    description=models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# defines the articles in the different categories

class Article(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=50, default=None)
    description=models.TextField()
    content=models.TextField()
    writer=models.CharField(max_length=100)
    Category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

