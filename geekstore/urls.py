"""geekstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import main, products_view, product_detail_view, category_view, create_products_view, ProductsView,\
    ProductDetailView, CategoryView, CreateProduct
from geekstore.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from users.views import LoginView, RegisterView, LogoutView #logout_view, login_view, register_view,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('products/', ProductsView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('products/create/', CreateProduct.as_view()),

    #users
    path('users/login/', LoginView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path('users/logout/', LogoutView.as_view()),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

