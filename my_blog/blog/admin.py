from django.contrib import admin

# Register your models here.
from blog.models import ArticleModel, NavModel




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','picture','nav1','nav2','author','issuedate','alterdate','sort','praise','is_show','is_Delete')
    list_editable = ['title']


class NavAdmin(admin.ModelAdmin):
    like_display = ('id', 'nav_name','Nav_root', 'issuedate', 'is_Show', 'is_Delete')

admin.site.register(ArticleModel, ArticleAdmin)

admin.site.register(NavModel, NavAdmin)