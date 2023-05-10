from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'opening_hours', 'tables', 'location']
