from .models import Exercise
from .models import User
from .models import Entry
from .serializers import ExerciseSerializer
from .serializers import UserSerializer
from .serializers import EntrySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .populate import data

#get all the exercises
#serialize them
#return json

#decorator from Django Rest Framework. 
#Indicates this view should only respond to GET requests.
@api_view(['GET'])
    #loop over data
        #pass each piece of data to serializer
        #if serializer is valid:
            #save to database

 #function that populates the database
 # will be called when a GET request is made to corresponding URL           
def populate_database(request):
    try:
        for i in data: #data is imported from populate.py
            # a new ExerciseSerializer instance is created for each item in data
            #serializer is used to convert the Python dictionary i into a format that can be saved to the database.
            serializer = ExerciseSerializer(data=i)
            if serializer.is_valid():
                #If data is valid,save it to the database.
                #creates a new Exercise object (or updates an existing one
                serializer.save()
        #If all items are processed without any errors...
        return Response("Success!!")
    
    except:
        return Response("Encountered Error during population")

# this view can handle both GET and POST requests
@api_view(['GET', 'POST'])
#optional format parameter
def exercise_list(request, format=None):

    if request.method == 'GET':
        #retrieves all Exercise objects from the database, ordered by their id
        exercises = Exercise.objects.all().order_by('id')
        #check if data is empty
        if not exercises.exists():
            #If database is empty,loop over each item in the data list (imported from populate.py)
            for i in data:
                #For each item, create a serializer
                serializer = ExerciseSerializer(data=i)
                if serializer.is_valid():
                    serializer.save()

                #Get all the Exercise objects from the database and sort 
                # them by their id in ascending order
                exercises = Exercise.objects.all().order_by('id')
        #creates a serializer for all the exercises. 
        # many=True argument indicates we're serializing multiple objects.
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
        else: return Response(status=status.HTTP_404_NOT_FOUND)

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