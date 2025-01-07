from django.urls import path, include
from .views import UserFileListView, TestAuthView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('files/', UserFileListView.as_view(), name='user-files'),
    path('test-auth/', TestAuthView.as_view(), name='test-auth'),
]
