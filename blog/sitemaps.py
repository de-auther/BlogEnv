from django.contrib.sitemaps import Sitemap
from .models import Blog



class BlogSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date


