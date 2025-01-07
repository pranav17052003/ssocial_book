# from django.shortcuts import render
# from django.http import JsonResponse
# import pandas as pd
# from sqlalchemy import create_engine




# # Create your views here.
# DATABASE_URL = "postgresql+psycopg2:myuser:mypassword//@localhost:5432/books"
# engine = create_engine(DATABASE_URL)

# def fetch_data(request):
#     query = "select * from books"
#     try:
#         with engine.connect() as connection:
#             result = pd.read_sql(query, connection)
        
#         data = result.to_dict(orient='records')
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, safe=False)

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserFile
from .serializers import UserFileSerializer

class UserFileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        files = UserFile.objects.filter(user=request.user)
        serializer = UserFileSerializer(files, many=True)
        return Response(serializer.data)


class TestAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated successfully!", "user": str(request.user)})





from django.shortcuts import render
from .models import UserFile
from .utils import user_has_uploaded_files
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

@login_required
@user_has_uploaded_files
def my_books_view(request):
    """
    Render the 'My Books' dashboard where the user can view uploaded files.
    """
    files = UserFile.objects.filter(user=request.user)
    return render(request, 'my_books.html', {'files': files})


@login_required
def upload_books_view(request):
    """
    Render the 'Upload Books' page for the user.
    """
    return render(request, 'upload_books.html')






from django.http import HttpResponseRedirect
from .models import UserFile
from django.urls import reverse

@login_required
def upload_books_view(request):
    """
    Render the 'Upload Books' page and handle file uploads.
    """
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            UserFile.objects.create(user=request.user, file=uploaded_file)
            return HttpResponseRedirect(reverse('my-books'))  # Redirect to 'My Books'
    return render(request, 'upload_books.html')