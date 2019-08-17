from django.conf.urls import url

from blog import views

urlpatterns = [


    url(r'^article/(\d+)$', views.article, name='article'),
    url(r'^about$', views.about, name='about'),
    url(r'^article_list/(\d+)$', views.article_list, name='article_list'),
    url(r'^$', views.index, name='index'),
]
app_name = 'blog'