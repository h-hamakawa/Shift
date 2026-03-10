from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('setup/', views.setup_view, name='setup'),
    path('home/', views.home_view, name='home'),

]