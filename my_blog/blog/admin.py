from django.contrib import admin

# Register your models here.
from blog.models import ArticleModel, NavModel ,PictureModel




class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','article_picture','nav1','nav2','author','issuedate','alterdate','sort','praise','is_show','is_Delete')
    list_editable = ['title']


class NavAdmin(admin.ModelAdmin):
    like_display = ('id', 'nav_name','Nav_root', 'issuedate', 'is_Show', 'is_Delete')



class PictureAdmin(admin.ModelAdmin):
    like_display = ('id', 'name','picture','issuedate', 'is_Show', 'is_Delete')


admin.site.register(ArticleModel, ArticleAdmin)

admin.site.register(NavModel, NavAdmin)

admin.site.register(PictureModel, PictureAdmin)