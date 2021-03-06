from django.conf.urls import url
from . import views

app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^data/avatar/(?P<member_name>.*)/$', views.avatar_view, name='avatar_view'),
    url(r'^members/$', views.member_view, name='member_view'),
    url(r'^members/(?P<member_name>.*)/$', views.member, name='member'),
    url(r'^post/img/$', views.post, name='post'),
    url(r'^threads/(?P<thread_name>.*)/$', views.thread, name='thread'),
    url(r'^registerUser/$', views.registerUser, name='registerUser'),
    url(r'^register/$', views.register, name='register'),
    url(r'^loginUser/$', views.loginUser, name='loginUser'),
    url(r'^login/$', views.signin, name='signin'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
]
