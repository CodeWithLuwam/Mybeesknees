from django.contrib import admin
from .models import Exercise
from .models import User
from .models import Entry

admin.site.register(Exercise)

admin.site.register(User)

admin.site.register(Entry)