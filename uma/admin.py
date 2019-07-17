"""
Register models for the admin panel.
"""
from .models.room import Room
from .models.roomcategory import RoomCategory
from django.contrib import admin

admin.site.register(Room)
admin.site.register(RoomCategory)
