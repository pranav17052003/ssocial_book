from django.urls import path, include
from .views import UserFileListView, TestAuthView
from .views import my_books_view, upload_books_view

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('files/', UserFileListView.as_view(), name='user-files'),
    path('test-auth/', TestAuthView.as_view(), name='test-auth'),
    path('my-books/', my_books_view, name='my-books'),
    path('upload-books/', upload_books_view, name='upload-books'),
]
