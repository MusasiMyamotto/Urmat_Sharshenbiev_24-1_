from django.shortcuts import render, redirect
from posts.models import Product, Review, Category
from posts.forms import ProductCreateForm, ReviewCreateForm
from django.views.generic import ListView, CreateView, DetailView



# Create your views here.

PAGINATION_LIMIT = 3


class MainView(ListView):
    model = Product
    template_name = 'layouts/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'layouts/index.html')


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, **kwargs):
        products = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            products = Product.objects.filter(
                name__icontains=search,
                description__icontains=search
            )

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        """ slice posts """
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1),
        }

        return render(request, self.template_name, context=context)


class ProductDetailView(DetailView, CreateView):
    model = Product
    template_name = 'products/detail.html'
    pk_url_kwarg = 'id'
    queryset = Product.objects.all()
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        return {
            'product': self.get_object(),
            'reviews': Review.objects.filter(product=self.get_object()),
            'form': kwargs.get('form', self.form_class)
        }

    def post(self, request, *args, **kwargs):
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                author_id=request.user.id,
                product_id=id,
                text=form.cleaned_data.get('text'),
            )
            return redirect(f'/products/{id}/')


class CategoryView(ListView):
    model = Category
    template_name = 'categories/index.html'

    def get(self, request, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, self.template_name, context=context)


class CreateProduct(ListView, CreateView):
    model = Product
    template_name = 'products/create.html'
    form = ProductCreateForm

    def get(self, request, **kwargs):
        context = {
            'form': ProductCreateForm,
        }
        return render(request, 'products/create.html', context=context)

    def post(self, request, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 5,
                quantity=form.cleaned_data.get('quantity'),
            )
            return redirect('/products/')
        return render(request, 'products/create.html', context={
            'form': form,
        })





#def main(request):
#    if request.method == 'GET':
#        return render(request, 'layouts/index.html')


# def products_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         search = request.GET.get('search')
#         page = int(request.GET.get('page', 1))
#
#         if search is not None:
#             products = Product.objects.filter(
#                 name__icontains=search,
#                 description__icontains=search
#             )
#
#         max_page = products.__len__() / PAGINATION_LIMIT
#         if round(max_page) < max_page:
#             max_page = round(max_page) + 1
#         else:
#             max_page = round(max_page)
#
#         """ slice posts """
#         products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
#
#         context = {
#             'products': products,
#             'user': request.user,
#             'max_page': range(1, max_page + 1),
#         }
#
#         return render(request, 'products/products.html', context=context)


# def category_view(request):
#      if request.method == 'GET':
#          categories = Category.objects.all()
#          context = {
#             'categories': categories,
#         }
#         return render(request, 'categories/index.html', context=context)

# def create_products_view(request):
#      if request.method == 'GET':
#          context = {
#              'form': ProductCreateForm,
#          }
#          return render(request, 'products/create.html', context=context)
#
#      if request.method == 'POST':
#          form = ProductCreateForm(request.POST, request.FILES)
#
#          if form.is_valid():
#              Product.objects.create(
#                  image=form.cleaned_data.get('image'),
#                  name=form.cleaned_data.get('name'),
#                  description=form.cleaned_data.get('description'),
#                  price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 5,
#                  quantity=form.cleaned_data.get('quantity'),
#              )
#              return redirect('/products/')
#         return render(request, 'products/create.html', context={
# #             'form': form,
#          })

# def product_detail_view(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == 'GET':
#         reviews = Review.objects.filter(product=product)
#
#         context = {
#             'product': product,
#             'reviews': reviews,
#             'form': ReviewCreateForm,
#         }
#         return render(request, 'products/detail.html', context=context)
#
#     if request.method == 'POST':
#         form = ReviewCreateForm(data=request.POST)
#
#         if form.is_valid():
#             Review.objects.create(
#                 author_id=request.user.id,
#                 product_id=id,
#                 text=form.cleaned_data.get('text'),
#             )
#             return redirect(f'/products/{id}/')
#         # return render(request, 'products/detail.html', context={
#         #     'product': product_obj,
#         #     'review': review,
#         #     'form': form
#         # })

