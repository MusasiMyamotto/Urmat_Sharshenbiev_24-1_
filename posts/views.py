from django.shortcuts import render, redirect
from posts.models import Product, Review, Category
from posts.forms import ProductCreateForm, ReviewCreateForm
from users.utils import get_user_from_request

# Create your views here.


def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html', context={'user': get_user_from_request(request)})


def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('categori_id')
        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))
        else:
            products = Product.objects.all()
        context = {
            'products': products,
            'user': get_user_from_request(request)
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':
        reviews = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': reviews,
            'form': ReviewCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=request.user.id,
                product_id=id,
                text=form.cleaned_data.get('text'),
            )
            return redirect(f'/products/{id}/')
        # return render(request, 'products/detail.html', context={
        #     'product': product_obj,
        #     'review': review,
        #     'form': form
        # })


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'user': get_user_from_request(request)
        }
        return render(request, 'categories/index.html', context=context)


def create_products_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm,
            'user': get_user_from_request(request)
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 5,
                quantity=form.cleaned_data.get('quantity'),

            )
            print('rate')
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form,
        })
