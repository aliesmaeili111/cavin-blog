from django.contrib import admin
from .models import Article,Category


# admin.site.site_header = "Calvin. Blog"

def make_published(modeladmin,request,queryset):
    
    rows_updated = queryset.update(status="p")
    if rows_updated ==1 :
        message_bit = ' منتشر شد.'
    else:
        message_bit = ' منتشر شدند'
    modeladmin.message_user(request,f"{rows_updated}مقاله {message_bit}")
    
make_published.short_description ="انتشار مقالات انتخاب شده"

    
def make_draft(modeladmin,request,queryset):
    
    rows_updated = queryset.update(status="d")
    if rows_updated ==1 :
        message_bit = ' پیش نویس شد.'
    else:
        message_bit = ' پیش نویس شدند'
    modeladmin.message_user(request,f"{rows_updated}مقاله {message_bit}") 
    
make_draft.short_description ="پیش نویس شدن مقالات انتخاب شده"    


class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('position','title','slug','status')
    list_display_links = ('position','title',)
    list_filter = (['status'])
    list_editable = ('status',)
    search_fields =  ('title','slug')
    prepopulated_fields = {'slug':('title',)}
   
admin.site.register(Category,CategoryAdmin) 



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','author','slug','publish','is_special','status','category_to_str')
    list_display_links = ('title','thumbnail_tag')
    list_filter = ('publish', 'status','author')
    list_editable = ('status','is_special',)
    search_fields =  ('title','descriptoin')
    prepopulated_fields = {'slug':('title',)} 
    ordering =['-status','-publish']
    actions = [make_published,make_draft]
    list_per_page = 6

    
    
    
admin.site.register(Article,ArticleAdmin)