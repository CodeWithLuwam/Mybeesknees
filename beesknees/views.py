from .models import Exercise
from .models import User
from .models import Entry
from .serializers import ExerciseSerializer
from .serializers import UserSerializer
from .serializers import EntrySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#get all the exercises
#serialize them
#return json



@api_view(['GET', 'POST'])
def exercise_list(request, format=None):

    if request.method == 'GET':
        exercises = Exercise.objects.all().order_by('id')
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def exercise_detail(request, id, format=None):

    try:
        exercise = Exercise.objects.get(pk=id)
    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ExerciseSerializer(exercise, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def user(request, format=None):

    if request.method == 'GET':
        user = User.objects.all().order_by('id')
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):

    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def entry(request, format=None):

    if request.method == 'GET':
        entry = Entry.objects.all().order_by('id')
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # print("inside of serializer") 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def entry_detail(request, id, format=None):

    try:
        entry = Entry.objects.get(pk=id)
    except Entry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EntrySerializer(entry)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EntrySerializer(entry, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)