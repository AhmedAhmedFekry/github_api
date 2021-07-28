from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from rest_framework.pagination import LimitOffsetPagination

def home(request):
    date= datetime.now() - timedelta(days=10)  
    date = date.strftime('%Y-%m-%d') 
    url = f'https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc'
    response = requests.get(url)
    response=response.json()
    # top three of repositories after filter
    three_of_repositories = response['items'][0:3]
 
    result = []
   
    for i in three_of_repositories:
        num_of_language = requests.get(f"https://api.github.com/search/repositories?q=language:{i['language']}").json()
        if i['language'] is  None:
            continue
        result.append({
            "html_url": i['html_url'],
            "language": {
            "name_language": i['language'],
            "number_of_repositories": num_of_language['total_count']
                }
            })
    return JsonResponse({'data':result})

class Home(APIView ):
  
    def get(self, request, format=None):

        date= datetime.now() - timedelta(days=10)  
        date = date.strftime('%Y-%m-%d') 
        url = f'https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&per_page=10'
        response = requests.get(url)
        response=response.json()
        # top three of repositories after filter
        three_of_repositories = response['items'][0:3]
    
        result = []
    
        for i in three_of_repositories:
            num_of_language = requests.get(f"https://api.github.com/search/repositories?q=language:{i['language']}").json()
            if i['language'] is  None:
                continue
            result.append({
                "html_url": i['html_url'],
                "name": i["name"],
                "language": {
                "name_language": i['language'],
                "number_of_repositories": num_of_language['total_count']
                    }
                })
        return Response(result)
