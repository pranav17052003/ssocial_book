from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .forms import CustomUserCreationForm
from .models import CustomUser
from .filters import UserFilter
from .forms import uploadBookForm
from .models import UploadedFile



# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def authors_and_sellers(request):
    user_filter = UserFilter(request.GET, queryset=CustomUser.objects.all()) 
    return render(request, 'authors_and_sellers.html', {'filter': user_filter})



def upload_books(request):
    if request.method == 'POST':
        form = uploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  
            uploaded_file.save()
            return redirect('uploaded_files')
    else:
        form = uploadBookForm()
    return render(request, 'upload_books.html', {'form': form})


def uploaded_files(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'files': files})
    