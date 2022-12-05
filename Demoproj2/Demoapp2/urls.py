from Demoapp2 import views
from django.urls import path
urlpatterns = [ path('', views.operationhandling, name='operationhandling'),
                path('add/', views.add, name='add') ]
#,
#                path('add/', views.add, name='add'),
#                path('sub/', views.sub, name='sub'),
#                path('mul/', views.mul, name='mul'),
#                path('div', views.div, name='div')