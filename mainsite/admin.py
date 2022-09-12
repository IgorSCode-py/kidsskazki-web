from django.contrib import admin

# Register your models here.
from .models import Book, Vote, Buyer

admin.site.register(Book)
admin.site.register(Vote)
admin.site.register(Buyer)