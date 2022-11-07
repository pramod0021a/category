from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def index_fun(request):
   all_products = None
   all_categories = Category.objects.all()
   categoryID = request.GET.get('category')
   if categoryID:
      all_products = Product.products_by_cat_id(categoryID)
   else:
      all_products = Product.objects.all()
   context = {
      'products': all_products,
      'categories': all_categories,
   }
   return render(request, 'mains/index.html', context)
   
   