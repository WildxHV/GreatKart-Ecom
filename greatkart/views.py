from django.shortcuts import render
from store.models import Product, ReviewRating


def home(request):
    products = Product.objects.all().filter(is_available = True)
    
    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products' : products,
        'reviews' : reviews
    }
    return render(request, 'home.html', context)

def custom_error_404(request, exception):
    return render(request, 'error/404error.html', status=404)


def custom_error_500(request):
    return render(request, 'error/500error.html', status=500)