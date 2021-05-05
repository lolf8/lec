from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('amaan',views.amaan,name='amaan'),
    path('david',views.david,name='david'),
    path('<str:name>',views.greet,name='greet'),
    
]