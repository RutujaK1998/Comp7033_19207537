from django.urls import path, include
from . import views
# staff/urls.py
from rest_framework import routers
from .views import StaffViewSet

router = routers.DefaultRouter()
router.register(r'staff', StaffViewSet)

app_name = 'staff'

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.staff_list, name='staff_list'),
    path('add/', views.staff_create, name='staff_create'),
    path('<int:pk>/', views.staff_detail, name='staff_detail'),
    path('<int:pk>/update/', views.staff_update, name='staff_update'),
    path('<int:pk>/delete/', views.staff_delete, name='staff_delete'),
]
