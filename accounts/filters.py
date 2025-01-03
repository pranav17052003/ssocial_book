# filters.py
import django_filters
from .models import CustomUser 

class UserFilter(django_filters.FilterSet):
    public_visibility = django_filters.BooleanFilter(field_name='public_visibility', label='Public Visibility', lookup_expr='exact')

    class Meta:
        model = CustomUser
        fields = ['public_visibility', 'username']  # Add any other fields you want to filter by
