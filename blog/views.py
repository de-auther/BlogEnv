from django.shortcuts import render,redirect, get_list_or_404
from .models import Blog, Category, Subscribers
from random import choice
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import get_template
import uuid
from .tasks import verify, notify, verified
from .adrf import test


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscribers.objects.filter(mail=email):
            messages.error(request,'emai already exists in our database!')

        else:
            #verify.delay(email)
            asyncio.run(test(email))
            messages.info(request,'You are Done!')
        return redirect('/')
    else:

        featured = Blog.objects.filter(featured=True)
        trending = Blog.objects.filter(trending=True)
        editorspick = Blog.objects.filter(editorspick=True)
        others =  Blog.objects.filter(featured=False, trending=False, editorspick=False)
        center = Blog.objects.filter(center=True)
        category = Category.objects.all()
        rnm1 = choice(category)
        random1 = Blog.objects.filter(category=rnm1)
        rnm2 = choice(category)
        random2 = Blog.objects.filter(category=rnm2)
        blogs = Blog.objects.all()


        return render(request, 'index.html', {'blogs': blogs, 'featured':featured, 'trending':trending, 'editorspick':editorspick, 'others':others, 'center':center, 'category':category, 'random1':random1, 'random2':random2, 'rnm1':rnm1, 'rnm2':rnm2})





def blog(request, c_slug, b_slug):
    pkc = get_list_or_404(Category, slug=c_slug)
    pkb = get_list_or_404(Blog, slug=b_slug)
    all = Blog.objects.all()
    blog = Blog.objects.get(category__slug=c_slug, slug=b_slug)
    category = Category.objects.all()
    return render(request, 'blog.html',{'blogs':blog, 'category':category, 'all':all})





def category(request, c_slug ):
    pk = get_list_or_404(Category, slug=c_slug)
    blog = Blog.objects.filter(category__slug=c_slug)
    category = Category.objects.all()
    recent = Blog.objects.all()
    path = request.path




    p = Paginator(blog, 10)
    total = p.num_pages
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        return redirect('home')






    return render(request, 'categories.html', {'blogs':page, 'category':category, 'name':c_slug, 'recent':recent, 'path':path, 'total':total})









def search(request):
    category = Category.objects.all()
    recent = Blog.objects.all()
    path = request.path
    query = request.POST.get('query')

    blog = Blog.objects.filter(Q(heading__icontains = query)|Q(header__contains = query))[:15]



    return render(request, 'categories.html', {'blogs':blog, 'category':category, 'recent':recent, 'path':path})





def about(request):
    category = Category.objects.all()
    return render(request, 'about.html', {'category':category})





def trends(request):
    category = Category.objects.all()
    trend = Blog.objects.filter(trending=True)
    recent = Blog.objects.all()
    path = request.path
    p = Paginator(trend, 10)
    total = p.num_pages
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        return redirect('home')
    return render(request, 'categories.html', {'blogs':page, 'category':category, 'recent':recent, 'path':path, 'total':total, 'name':'Trends'})





def recents(request):
    category = Category.objects.all()
    recent = Blog.objects.all().order_by('-date')
    recent = Blog.objects.all()
    path = request.path
    p = Paginator(recent, 10)
    total = p.num_pages
    page_num = int(request.GET.get('page', 1))


    try:
        page = p.page(page_num)
    except EmptyPage:
        return redirect('home')
    return render(request, 'categories.html', {'blogs':page, 'category':category, 'recent':recent, 'path':path, 'total':total, 'name':'Recents'})






def contentNotify(request):



    # users = []
    # for email in User.objects.all():
    #     users.append(email.email)





    # mail = EmailMultiAlternatives(
    #                 subject='New Content Alert: Stay Up-to-Date with Our Latest Releases!',
    #                 from_email = 'support.careerenv.com',
    #                 bcc = users

    #     )


    # html = get_template("email.html").render()
    # mail.attach_alternative(html, "text/html")
    # mail.send()



    notify.delay()

    messages.info(request,'You are Done!')
    return redirect('/')






def emailVarify(request, link):
    
    if Subscribers.objects.filter(id=link).exists():
        sub = Subscribers.objects.get(id=link)
        verified.delay(link)
        return render(request, 'subscriber.html', {'link':link, 'sub':sub})
    else:
        return redirect('/')


def addInterest(request):
    user = Subscribers.objects.get(id =request.GET.get('link'))
    user.intrest1 = request.GET.get('interest1')
    user.intrest2 = request.GET.get('interest2')
    user.intrest3 = request.GET.get('interest3')
    user.save()

    return redirect('/')
    