from django.shortcuts import render
from rest_framework.response import Response
from rest_framework. request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import TaskModelSerializer
from .models import TaskModel

# Create your views here.

@api_view(http_method_names=["GET"])
def home(request:Request):
    content = {"message":"This is the homepage view. Now we good to get started creating our tasks"}
    return Response(data=content, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST"])
def list_tasks(request: Request):
    tasks = TaskModel.objects.all()
    
    if request.method == "POST":
        data = request.data
        
        serializer = TaskModelSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message": "Task Created Succesfully",
                "data": serializer.data
            }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = TaskModelSerializer(instance=tasks, many=True)
    response = {
        "message": "tasks",
        "data":serializer.data
    }
    
    return Response(data=response, status = status.HTTP_200_OK)
    
    
@api_view(http_method_names=["GET", "POST"])
def task_detail(request: Request, task_id: int):
    task = get_object_or_404(TaskModel, pk=task_id)
    
    serializer = TaskModelSerializer(instance=task)
    response = {
        "message": "Task " + str(task_id) + " details",
        "data": serializer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)
    
@api_view(http_method_names=["PUT"])
def update_task(request:Request, task_id: int):
    task = get_object_or_404(TaskModel, pk=task_id)
    
    data = request.data
    
    serializer = TaskModelSerializer(instance=task, data=data)
    
    if serializer.is_valid():
        serializer.save()
        
        response={
            "message": "Updated Task " + str(task_id) + " Succesfully",
            "data": serializer.data
        }
        
        return Response(data=response, status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def delete_task(request:Request, task_id: int):
    task = get_object_or_404(TaskModel, pk=task_id)
    
    task.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)



    
    