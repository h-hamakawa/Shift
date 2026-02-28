from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .models import AdminSetting
from .forms import AdminSetupForm


def index_view(request):

    if AdminSetting.objects.exists():
        return redirect('home')
    return redirect('setup')


def setup_view(request):

    if AdminSetting.objects.exists():
        return redirect('home')

    if request.method == 'POST':
        form = AdminSetupForm(request.POST)
        if form.is_valid():
            AdminSetting.objects.create(
                employee_number=form.cleaned_data['employee_number'],
                password=make_password(form.cleaned_data['password']),
            )
            return redirect('home')
    else:
        form = AdminSetupForm()

    return render(request, 'accounts/setup.html', {'form': form})


def home_view(request):

    if not AdminSetting.objects.exists():
        return redirect('setup')
    return render(request, 'accounts/home_placeholder.html')
