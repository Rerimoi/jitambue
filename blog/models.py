from django.conf import settings
from django.db import models
from django.utils import timezone

# user profile model
# class UserProfileInfo(models.Model):

#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
#     def __str__(self):
#         return self.user.username

# defines each category in SRH i.e GBV,Abortion, Hygiene
class Category(models.Model):
    # image=models.ImageField()
    name= models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# defines the articles in the different categories

class Article(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=50, default=None)
    content=models.TextField()
    writer=models.CharField(max_length=100)
    Category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

