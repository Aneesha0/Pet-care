from django.contrib import admin

from .models import Book,Service,Status,Pet


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Owner Information', {'fields': ['owners','owner']}),
        ('Pet Information', {'fields': ['pet_name','animal']}),
        ('Date information', {'fields': ['date','time']}),
        ('Choice of Booking', {'fields': ['services']}),
        ('State of Booking', {'fields': ['statuses']}),
    ]   
    readonly_fields=('time','owners','owner','pet_name','animal','services','date')
    list_display=('owners','owner','pet_name','animal','services','statuses','date','time')
    list_filter = ['statuses','services','date','time','animal']
    search_fields = ['owners__username']

admin.site.register(Book,BookAdmin)
admin.site.register(Service)
admin.site.register(Status)
admin.site.register(Pet)
