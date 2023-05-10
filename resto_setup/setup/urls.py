from django.urls import path, include
from . import views
from rest_framework import routers
app_name = 'setup'

from rest_framework import routers
from .views import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'setup', RestaurantViewSet)

app_name = 'setup'

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.restaurant_list, name='restaurant_list'),
    path('add/', views.restaurant_create, name='restaurant_create'),
    path('<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
]

# urlpatterns = [
#     path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
#     # path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
# ]

