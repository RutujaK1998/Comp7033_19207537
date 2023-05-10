from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .forms import RestaurantForm
from setup.models import Restaurant
from .serializers import RestaurantSerializer
from django.shortcuts import render, redirect


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'setup/restaurant-list.html', {'setup': restaurant})

def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('setup:restaurant_list')
    return render(request, 'setup/restaurant-form.html', {'form': form})

def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('setup:restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'setup/restaurant-form.html', {'form': form})

@api_view(['GET'])
def restaurant_detail(request, pk):
    restaurant_member = get_object_or_404(Restaurant, pk=pk)
    serializer = RestaurantSerializer(restaurant_member)
    return Response(serializer.data)



