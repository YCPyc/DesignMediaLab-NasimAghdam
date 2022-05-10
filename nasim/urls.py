from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('detail/biography/<str:pk>',views.Biography,name="Biography"),
    path('detail/animal/<str:pk>',views.Animal,name="Animal"),
    path('detail/veganism/<str:pk>',views.Veganism,name="Veganism"),
    path('detail/immigration/<str:pk>',views.Immigration,name="Immigration"),
    path('detail/family/<str:pk>',views.Family,name="Family"),

]