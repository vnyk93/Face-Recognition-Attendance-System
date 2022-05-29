from django.contrib import admin
from .models import *
#To register profile model
admin.site.register(Profile)
#To redister last face
admin.site.register(LastFace)