from django.shortcuts import render
from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['DELETE'])
def delete_by_id(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # delete a single employee
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all(request):
    if request.method == 'GET':
        employees = User.objects.all()
        serializer = UserSerializer(employees, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add(request):
    if request.method == 'POST':
        data = {
            "uid": request.data.get('uid'),
            "uname": request.data.get('uname'),
            "uemail": request.data.get('uemail'),
            "upassword": request.data.get('upassword'),
            "ucontact": request.data.get('ucontact')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_id(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single employee
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def get_update_edit(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        # update details of a single employee
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Tham khao

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_employee(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single employee
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # update details of a single employee
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single employee
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def get_post_employee(request):
    # get all employee
    if request.method == 'GET':
        employees = User.objects.all()
        serializer = UserSerializer(employees, many=True)
        return Response(serializer.data)
    # insert a new record for a employee
    if request.method == 'POST':
        data = {
            "uid": request.data.get('uid'),
            "uname": request.data.get('uname'),
            "uemail": request.data.get('uemail'),
            "upassword": request.data.get('upassword'),
            "ucontact": request.data.get('ucontact')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API_objects(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
