import django_filters
from django.db.models import Q

from shop.models import Category, Product


class ProductFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), field_name='categories')
    price = django_filters.RangeFilter()
    search = django_filters.CharFilter(method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))

    class Meta:
        model = Product
        fields = ['categories', 'price', 'search']
