from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^signin', views.signin, name='signin'),
    url(r'^signup_page', views.signup_page, name='signup_page'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^signout', views.signout, name='signout'),
    url(r'^comment_form', views.post_comment_form, name='comment_form'),
    url(r'^send', views.post_send, name='post_send')
]