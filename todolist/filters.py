import django_filters
from .models import Category





class CategoryFilter(django_filters.FilterSet):
    category_name = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    class Meta:
        model = Category
        fields = ['category_name']
        


