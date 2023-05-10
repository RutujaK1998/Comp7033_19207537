from django.urls import path
from . import views

app_name = 'manager_dashboard'

urlpatterns = [
  
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
