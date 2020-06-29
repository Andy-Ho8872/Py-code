from django.urls import path
from . import views     #  . means the current folder


#/product   is the root of urls
# ex: /product/xxx/detail   or  /products/1234

urlpatterns = [
    path('', views.index) ,  # to delegate to the page
    path('new', views.new)
]