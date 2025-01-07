from django.shortcuts import redirect
from .models import UserFile

def user_has_uploaded_files(view_func):
    
    def wrapper(request, *args, **kwargs):
        if not UserFile.objects.filter(user=request.user).exists():
            return redirect('upload_books')
        return view_func(request, *args, **kwargs)
    return wrapper
