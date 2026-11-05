from django.contrib import admin
from .models import Director, DirectorProfile, Genre, Actor, Movie, Review

admin.site.register(Director)
admin.site.register(DirectorProfile)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Review)
