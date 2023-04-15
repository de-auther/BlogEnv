from django.db import models
from django.urls import reverse
import uuid

# Create your models here.




class Category(models.Model):
    category = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.category


    def get_category(self):
        return reverse('category', args=[self.slug])






class Blog(models.Model):
    previous = models.TextField(null=True, blank=True)


    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    editorspick = models.BooleanField(default=False)
    center =  models.BooleanField(default=False)

    banner = models.TextField(null=True, blank=True)

    heading = models.CharField(max_length=200, blank=True, null=True)
    header = models.TextField(null=True, blank=True)
    ytswitch = models.BooleanField(default=False)
    ytlink = models.TextField(null=True, blank=True)
    credit0 = models.CharField(max_length=100, null=True, blank=True)
    linkd1 = models.TextField(null=True, blank=True)
    link1 = models.TextField(null=True, blank=True)

    h1 = models.CharField(max_length=200, null=True, blank=True)
    p1 = models.TextField(null=True, blank=True)
    qt1 = models.TextField(null=True, blank=True)
    pic1 = models.TextField(null=True, blank=True)
    credit1 = models.CharField(max_length=100, null=True, blank=True)
    linkd2 = models.TextField(null=True, blank=True)
    link2 = models.TextField(null=True, blank=True)

    h2 = models.CharField(max_length=200, null=True, blank=True)
    p2 = models.TextField(null=True, blank=True)
    qt2 = models.TextField(null=True, blank=True)
    pic2 = models.TextField(null=True, blank=True)
    credit2 = models.CharField(max_length=100, null=True, blank=True)
    linkd3 = models.TextField(null=True, blank=True)
    link3 = models.TextField(null=True, blank=True)

    h3 = models.CharField(max_length=200, null=True, blank=True)
    p3 = models.TextField(null=True, blank=True)
    qt3 = models.TextField(null=True, blank=True)
    pic3 = models.TextField(null=True, blank=True)
    credit3 = models.CharField(max_length=100, null=True, blank=True)
    linkd4 = models.TextField(null=True, blank=True)
    link4 = models.TextField(null=True, blank=True)

    h4 = models.CharField(max_length=200, null=True, blank=True)
    p4 = models.TextField(null=True, blank=True)
    qt4 = models.TextField(null=True, blank=True)
    pic4 = models.TextField(null=True, blank=True)
    credit4 = models.CharField(max_length=100, null=True, blank=True)
    linkd5 = models.TextField(null=True, blank=True)
    link5 = models.TextField(null=True, blank=True)

    h5 = models.CharField(max_length=200, null=True, blank=True)
    p5 = models.TextField(null=True, blank=True)
    qt5 = models.TextField(null=True, blank=True)
    pic5 = models.TextField(null=True, blank=True)
    credit5 = models.CharField(max_length=100, null=True, blank=True)
    linkd6 = models.TextField(null=True, blank=True)
    link6 = models.TextField(null=True, blank=True)

    footer = models.TextField(null=True, blank=True)
    linkd7 = models.TextField(null=True, blank=True)
    link7 = models.TextField(null=True, blank=True)

    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)

    next = models.TextField(null=True, blank=True)

    timetoread = models.CharField(blank=True, null=True, max_length=50)



    class Meta:
        ordering = ['-date']



    def __str__(self):
        return self.heading



    def get_blog(self):
        return reverse('blog', args=[self.category.slug, self.slug])

    def get_absolute_url(self):
        return reverse('blog', args=[self.category.slug, self.slug])





class Subscribers(models.Model):
    mail = models.CharField(max_length=150, blank=True, null=True)
    intrest1 = models.TextField(blank=True, null=True)
    intrest2 = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return self.mail
