from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product/product.html')



def product_details(request):
    return render(request, 'product/product_details.html')


def order_details(request):
    return render(request, 'product/order_details.html')