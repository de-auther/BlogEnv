"""blogenv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap

app_name = "blog"


sitemaps = {
    'blog':BlogSitemap
}





urlpatterns = [
    path('fuckingadmin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search-blog/', views.search, name='search'),
    path('about-me/', views.about, name='about'),
    path('trending/', views.trends, name='trends'),
    path('recents/', views.recents, name='recents'),
    path('fuckingnotify/', views.contentNotify),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('adding-interest/', views.addInterest, name="addinterest"),
    path('email-varification/<slug:link>/', views.emailVarify),
    path('<slug:c_slug>/', views.category, name='category'),
    path('<slug:c_slug>/<slug:b_slug>/', views.blog, name='blog'),
    

]
