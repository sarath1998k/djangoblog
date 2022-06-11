from . import views
from django.urls import path,include
app_name='blogapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:c_slug>/',views.allCat,name='blogs_by_category'),
    path('<slug:c_slug>/<slug:b_slug>/',views.blog,name='blog'),
]