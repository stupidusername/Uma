"""
Register models for the admin panel.
"""
from .models.article import Article
from .models.articlecategory import ArticleCategory
from .models.room import Room
from .models.roomcategory import RoomCategory
from django.contrib import admin

admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(Room)
admin.site.register(RoomCategory)
