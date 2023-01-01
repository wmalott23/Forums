from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ThreadSerializer
from .models import Thread

# Create your views here.

@api_view(['GET', 'POST'])
def thread_list(request):
    if request.method == 'GET':
        threads = Thread.objects.all()
        serializers = ThreadSerializer(threads, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ThreadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'GET':
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ThreadSerializer(thread, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)