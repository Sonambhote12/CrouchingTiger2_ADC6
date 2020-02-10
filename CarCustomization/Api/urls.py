from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('Apis/',getter),
    path('Apis/<int:ID>',getter_by_id),
    path('Apis/Page/<int:PAGENO>/',Api_CarCustomization_pagination, name = "Api_CarCustomization_Pagination"),

    # path('Apis/<int:ID>',views.deleter),


    # path('',include('Api.urls'))

]