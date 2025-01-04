from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
# from .forms import CustomUserCreationForm
from .models import CustomUser
from .filters import UserFilter
# from .forms import uploadBookForm
# from .models import UploadedFile


from django.contrib.auth.decorators import login_required
# from .models import UploadedFile
from django.utils.timezone import now
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request, 'index.html') 


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


def forgot_password(request):
    return render(request,'forgot-password.html')

def dashboard(request):
    return render(request,'dashboard.html')


def logout_view(request):
    # Logout logic
    logout(request)
    return redirect('login')

def authors_and_sellers(request):
    user_filter = UserFilter(request.GET, queryset=CustomUser.objects.all()) 
    return render(request, 'authors_and_sellers.html', {'filter': user_filter})




from .models import UploadedFile
from .forms import UploadFileForm
# @login_required
def uploaad_books(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        visibility = request.POST['visibility']
        cost = request.POST.get('cost', None)
        year_published = request.POST['year_published']
        file = request.FILES['file']

        # Save the uploaded file
        UploadedFile.objects.create(
            user=request.user,
            title=title,
            description=description,
            visibility=visibility,
            cost=cost,
            year_published=year_published,
            file=file
        )
        return redirect('uploaded_files')
    
    return render(request, 'upload_books.html')



# @login_required
def uploaded_files(request):
    # Fetch files uploaded by the logged-in user
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'uploaded_files': uploaded_files})