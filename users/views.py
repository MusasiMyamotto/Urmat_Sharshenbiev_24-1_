from django.shortcuts import render, redirect
from users.forms import AuthForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, RedirectView


# Create your views here.

class LoginView(ListView, CreateView):
    template_name = 'users/login.html'

    def get(self, request, **kwargs):
        context = {
            'form': AuthForm(),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        form = AuthForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'чувак попробуй дагы бир жолу')

        return render(request, 'users/login.html', context={
            'form': form,
        })


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/products/')


class RegisterView(ListView, CreateView):
    template_name = 'users/register.html'

    def get(self, request, **kwargs):
        context = {
            'form': RegisterForm,
        }
        return render(request, 'users/register.html', context=context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
            if password1 == password2:
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login/')
            else:
                form.add_error('password1', 'ошибка')

        return render(request, 'users/register.html', context={
            'form': form,
        })



#def login_view(request):
#    if request.method == 'GET':
#        context = {
#            'form': AuthForm(),
#        }
#        return render(request, 'users/login.html', context=context)
#    if request.method == 'POST':
#        form = AuthForm(data=request.POST)

#        if form.is_valid():
#            user = authenticate(
#                username=form.cleaned_data.get('username'),
#                password=form.cleaned_data.get('password')
#            )
#            if user:
#                login(request, user)
#                return redirect('/products/')
#            else:
#                form.add_error('username', 'чувак попробуй дагы бир жолу')

#        return render(request, 'users/login.html', context={
#            'form': form,
#        })

#def logout_view(request):
#    logout(request)
#    return redirect('/products/')


#def register_view(request):
#    if request.method == 'GET':
#        context = {
#            'form': RegisterForm,
#        }
#        return render(request, 'users/register.html', context=context)

#    if request.method == 'POST':
#        form = RegisterForm(data=request.POST)

#        if form.is_valid():
#            password1, password2 = form.cleaned_data.get('password1'), form.cleaned_data.get('password2')
#            if password1 == password2:
#                User.objects.create_user(
#                    username=form.cleaned_data.get('username'),
#                    password=form.cleaned_data.get('password1')
#                )
#                return redirect('/users/login/')
#            else:
#                form.add_error('password1', 'ошибка')

#        return render(request, 'users/register.html', context={
#            'form': form,
#        })