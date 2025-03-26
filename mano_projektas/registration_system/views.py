from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})

def users(request):
    users = User.objects.all().order_by('-register_date')
    return render(request, 'users.html', {'users': users})

# Create your views here.
