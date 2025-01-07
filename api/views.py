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
