from django.contrib import admin
from .models import Category, Article,UserProfileInfo


# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(UserProfileInfo)
admin.site.site_header="Jitambue"
admin.site.site_title="Jitambue"