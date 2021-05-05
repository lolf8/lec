from django.urls import path
from . import views

app_name='tasker'
urlpatterns=[
    path('',views.tasks,name='tasks'),
    path('time',views.show,name='show'),
    path('<str:name>',views.greet,name='greet'),
]