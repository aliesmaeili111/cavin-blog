from django.contrib import admin
from .models import Contact



class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('id','name','email')
    list_display_links = ('id','name','email')
    list_filter=('name','email')
    search_fields = ('id','name','email')
    list_per_page = 15


admin.site.register(Contact,ContactAdmin)