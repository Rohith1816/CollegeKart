from django.utils.timezone import datetime
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from .models import Contact
from .forms import sale
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    dests_list = Product.objects.all().order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 8)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'dests': dests })
    #cat = Categories.ob
    

def sell(request):
    if request.method=='POST':
        form=sale(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            owner = form.cleaned_data['owner']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            p = Product(name=name, owner=owner, description= description, category= category, price= price, image=image, created=datetime.now())
            p.save()
    else:
        form=sale()
    context={
        'form':form.as_p()
    }
    return render(request,'sell.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Login failed')
            return redirect('login')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Registration Failed')
            return redirect('register')

    else:
        return render(request, 'register.html')




def mobile(request):
    dests_list = Product.objects.filter(category__id= 3).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'mobile.html', { 'dests': dests })

def ed(request):
    dests_list = Product.objects.filter(category__id= 6).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'ed.html', { 'dests': dests })

def apron(request):
    dests_list = Product.objects.filter(category__id= 7).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'apron.html', { 'dests': dests })

def books(request):
    dests_list = Product.objects.filter(category__id= 4).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'books.html', { 'dests': dests })

def coolar(request):
    dests_list = Product.objects.filter(category__id= 9).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'coolar.html', { 'dests': dests })

def electronic(request):
    dests_list = Product.objects.filter(category__id= 8).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'electronic.html', { 'dests': dests })

def laptop(request):
    dests_list = Product.objects.filter(category__id= 2).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'laptop.html', { 'dests': dests })

def others(request):
    dests_list = Product.objects.filter(category__id= 11).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'others.html', { 'dests': dests })

def stationery(request):
    dests_list = Product.objects.filter(category__id= 10).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'stationery.html', { 'dests': dests })

def vehicle(request):
    dests_list = Product.objects.filter(category__id= 5).order_by('-created')
    page = request.GET.get('page', 1)
    paginator = Paginator(dests_list, 4)
    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, 'vehicle.html', { 'dests': dests })


def single(request, id):
    product = get_object_or_404(Product,
                                id=id)
    return render(request,'single.html',{'product': product}) 

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        subject= request.POST['subject']
        username= request.POST['username']
        message= request.POST['message']

        user = auth.authenticate(username=username)
        if User.objects.filter(username=username).exists():
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                subject = form.cleaned_data['subject']
                username = form.cleaned_data['username']
                message = form.cleaned_data['message']
                p = Contact(first_name=first_name, last_name=last_name, subject= subject, username= username, message= message)
                p.save()
                
            else:
                messages.info(request,'Message Sent')
                return redirect('home:contact')
        else:
            messages.info(request, 'Incorrect Username')
            return redirect('home:contact')

    else:
        form= ContactForm()
        
    context={
        'form':form.as_p()
    }
    return render(request,'contact.html',context)


# def search(request):
#     qer=request.GET.get('search')
#     desti=Product.objects.filter(name__contains =qer )
#     return render(request,'search.html',{'desti':desti})
