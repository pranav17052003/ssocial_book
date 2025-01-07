from django.urls import path
from .views import dashboard, forgot_password, login_view, logout_view, register_view, index, authors_and_sellers;
from .views import uploaad_books, uploaded_files
urlpatterns = [
    path('', index , name='index'), 
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('forgot-password/', forgot_password ,name='forgot_password'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('authors-sellers/', authors_and_sellers, name='authors_and_sellers'),
    path('uploaad-books/, ', uploaad_books, name='uploaad_books'),
    path('uploaded-files/', uploaded_files, name='uploaded_files'),
    
]
