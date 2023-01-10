from django.shortcuts import render
from rest_framework.response import Response
from rest_framework. request import Request
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(http_method_names=["GET"])
def home(request:Request):
    content = {"message":"This is the homepage view. Now we good to get started creating our tasks"}
    return Response(data=content, status=status.HTTP_200_OK)
