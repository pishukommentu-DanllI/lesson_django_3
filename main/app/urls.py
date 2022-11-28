from django.urls import path, include, re_path
from . import views

post_patterns = [
    path('popular', views.popular),
    path('new_post', views.new_post),
    path('all', views.post),
    re_path(r'^like/(?P<id>\d+)', views.number_post_like),
    re_path(r'^like', views.number_post_like),
    re_path(r'^comments/(?P<id>\d+)', views.number_post_comments),
]


urlpatterns = [
    path('', views.index),
    path('post/', include(post_patterns)),
    path('about', views.about_first),
    path('about_second', views.about_second),
    path('contacts', views.contacts_first),
    path('contacts_second/', views.contacts_second),
    path('access', views.access),
    path('json', views.json),
    path('set', views.set),
    path('get', views.get),
    re_path(r'^', views.pageNotFound)
]
