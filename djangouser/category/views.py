from django.shortcuts import render, redirect
from . forms import CategoryForm, SubCategoryForm
from . models import Category, SubCategory

# Create your views here.
def view(request):
    cats = Category.objects.all()
    return render(request, 'category/view.html', {'data': cats})

def view_subcategories(request, id):
    subcats = SubCategory.objects.filter(category__id = id)
    return render(request, 'category/subcategories.html', {'data': subcats})

def create(request):
    if request.method == "GET":
        return render(request, 'category/create.html', {'form': CategoryForm()})
    else:
        cf = CategoryForm(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect('view_category')
        else:
            return render(request, 'category/create.html', {'form': cf})

def create_subcategory(request):
    if request.method == "GET":
        return render(request, 'subcategory/create.html', {'form': SubCategoryForm()})
    else:
        scf = SubCategoryForm(request.POST)
        if scf.is_valid():
            scf.save()
            return redirect('view_category')
        else:
            return render(request, 'category/create.html', {'form': scf})
