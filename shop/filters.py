import django_filters

from shop.models import Category, Product


class ProductFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), field_name='categories')

    class Meta:
        model = Product
        fields = ['categories']
