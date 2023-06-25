from django.contrib import admin
from .models import book,bookcategory
# Register your models here.
class showcategory(admin.ModelAdmin):
    list_display = ["catname"]
admin.site.register(bookcategory,showcategory)

class showbook(admin.ModelAdmin):
    list_display = ['bookname','category','price']
admin.site.register(book,showbook)