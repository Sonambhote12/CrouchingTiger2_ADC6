# from django.contrib import admin
from django.urls import path, include   
from django.conf.urls import url
from .views import *

app_name='Carcustomizations'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',contact,name='contact'),

    path('search/',search,name='search'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name="register"),
    path('logout/', logout_page, name='logout'),
    # path('login1,',login1,name='login1')
    path('order_list',order_list,name='order_list')


]

# urlpatterns += [
#     # path('accounts/',include('django.contrib.auth.urls')),
#     path('accounts/login/',view_authenticate_user)

# ]
