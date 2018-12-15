from django.urls import path,re_path
from .views import create_or_retrieve,update_member
app_name = 'rest_api'
urlpatterns = [
	re_path(r'^member/(?P<pk>\d+)/$',create_or_retrieve,name='create'),
    re_path(r'^member/(?P<pk>\d+)/$',update_member,name='update'),
    path('member/',create_or_retrieve,name='retrieve' ),
    
 ]