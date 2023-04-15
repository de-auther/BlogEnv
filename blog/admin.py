from django.contrib import admin
from blog.models import *




class Categ_admin(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('category',)}


class Blog_admin(admin.ModelAdmin):
    prepopulated_fields =  {'slug':('heading',)}




admin.site.register(Subscribers)

admin.site.register(Category, Categ_admin)

admin.site.register(Blog, Blog_admin)