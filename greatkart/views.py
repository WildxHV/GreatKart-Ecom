from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products' : products,
    }
    return render(request, 'home.html', context)

def custom_error_404(request, exception):
    return render(request, 'error/404error.html', status=404)


def custom_error_500(request):
    return render(request, 'error/500error.html', status=500)