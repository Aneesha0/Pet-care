from django.contrib import admin

from .models import Book,Service,Status

admin.site.register(Book)
admin.site.register(Service)
admin.site.register(Status)
# admin.site.register(Pet)
