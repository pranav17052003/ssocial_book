from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from sqlalchemy import create_engine




# Create your views here.
DATABASE_URL = "postgresql+psycopg2://books:books@localhost:5432/books"
engine = create_engine(DATABASE_URL)

def fetch_data(request):
    query = "select * from books"
    try:
        with engine.connect() as connection:
            result = pd.read_sql(query, connection)
        
        data = result.to_dict(orient='records')
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False)
