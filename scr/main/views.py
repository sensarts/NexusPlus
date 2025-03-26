from django.shortcuts import render
from django.db.models import Prefetch
from category.models import Category, Region
from product.models import Product, ProductImage

def main(request):
    categories = Category.objects.filter(is_main=True)
    regions = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))

    ctx = {
        "categories": categories,
        "regions": regions,
        "products": products,
    }
    return render(request, 'index-2.html', ctx)