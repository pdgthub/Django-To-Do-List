
from django.shortcuts import render
from .models import Category, Item
from .filters import CategoryFilter
from .forms import ItemForm, CategoryForm
from django.shortcuts import redirect


# Create your views here.
def todolist(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    myFilter = CategoryFilter(request.GET, queryset=categories)
    categories = myFilter.qs
    return render(request, 'todolist/list.html', {'categories': categories, 'myFilter': myFilter, 'items': items})


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todolist')
    else:
        form = ItemForm()
    return render(request, 'todolist/add_item.html', {'form': form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('todolist')
    else:
        form = CategoryForm()
    return render(request, 'todolist/add_category.html', {'form': form})

def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('todolist')
    return render(request, 'todolist/delete_category.html', {'object': category} )

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('todolist')
    return render(request, 'todolist/delete_item.html', {'object': item} )