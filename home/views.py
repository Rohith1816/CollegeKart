from django.shortcuts import render
from product.models import Product
from .forms import sale

def index(request):
    dests = Product.objects.all()
    #cat = Categories.ob
    return render(request, 'index1.html',{'dests': dests})

def sell(request):
    if request.method=='POST':
        form1=sale(request.POST)
        if form1.is_valid :
            form1.as_p().save()
    else:
        form1=sale()
    context={
        'form':form1.as_p()
    }
    return render(request,'sell.html',context)
def search(request):
    qer=request.GET.get('search')
    desti=Product.objects.filter(name__contains =qer )
    return render(request,'search.html',{'desti':desti})
def vsearch(request):
    qer=request.GET.get('vsearch')
    desti=[ item for item in Product.objects.all() if  item.price == 344 and qer in item.name.lower() ]
    return render(request,'search.html',{'desti':desti})
def vehicle(request):
    dests=[item for item in Product.objects.all() if item.price == 344]
    return render(request,'vehicles.html',{'dests':dests})