from django.urls import path
from .views import register_view, login_view
from .views import authors_and_sellers, upload_books, uploaded_files

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('authors-sellers/', authors_and_sellers, name= 'authors_and_sellers'),
    path('upload-books/', upload_books, name='upload_books'),
    path('uploaded-files/', uploaded_files, name='uploaded_files')
    
]