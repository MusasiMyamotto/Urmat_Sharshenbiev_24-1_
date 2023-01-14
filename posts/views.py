from django.shortcuts import render
from posts.models import Product

#from datetime import datetime

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
           'products': products
        }

        return render(request, 'products/products.html', context=context)



#def hello(request):
#    if request.method == 'GET':
#        return HttpResponse('hello! its my project')

#def now_date(request):
#    now = datetime.now()
#    if request.method == 'GET':
#        return HttpResponse(f'The current date is {now}')

#def goodby(request):
#    if request.method == 'GET':
#        return HttpResponse('Goodby user')