from django.urls import path
from . import views
app_name = 'home'
urlpatterns=[
    path('',views.index,name='index'),
    path( 'sell',views.sell,name='sell'),
    path('search/',views.search,name='search'),
    path('vsearch/',views.vsearch,name='vsearch'),
    path('vehicle',views.vehicle,name='vehicle'),
]