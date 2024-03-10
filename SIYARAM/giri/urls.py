from django.urls import  path,include
from .views import *
urlpatterns=[
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('gir/',gir,name='gir'),
    path('signup/',signup,name='signup'),
    path('signup1/', signup1, name='signup1'),

]