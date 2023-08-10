from rest_framework import serializers
from .models import Exercise
from .models import User
from .models import Entry

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Exercise
        fields=['id', 'name', 'description', 'image']

class UserSerializer(serializers.ModelSerializer):
    #This field will call the get_entries method to provide a 
    # customized representation of the entries for each user.
    entries = serializers.SerializerMethodField()

    class Meta:
        model= User
        fields=['id', 'name', 'email', 'entries']

    #retrieves the related entries for the user and then uses
    # the EntrySerializer to serialize each entry.
    def get_entries(self, user):
        entries = Entry.objects.filter(user=user)
        entry_serializer = EntrySerializer(entries, many=True)
        return entry_serializer.data

class EntrySerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=True, read_only=True)

    class Meta:
        model= Entry
        fields=['id', 'date', 'sets', 'reps_or_mins', 'user', 'exercise']
