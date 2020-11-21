from django.urls import path
from . import views
app_name = 'home'
urlpatterns=[
    path('',views.index,name='index'),
    path( 'sell',views.sell,name='sell'),
    path('mobile', views.mobile, name='mobile'),
    path('apron', views.apron, name='apron'),
    path('books', views.books, name='books'),
    path('coolar', views.coolar, name='coolar'),
    path('ed', views.ed, name='ed'),
    path('electronic', views.electronic, name='electronic'),
    path('laptop', views.laptop, name='laptop'),
    path('others', views.others, name='others'),
    path('stationery', views.stationery, name='stationery'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('single/<int:id>/', views.single, name='single'),
    path( 'about',views.about,name='about'),
    path( 'contact',views.contact,name='contact'),
    # path('search/',views.search,name='search'),
    # path('vsearch/',views.vsearch,name='vsearch'),
    
]