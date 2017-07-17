from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/entity/$', views.EntityList.as_view(), name='name'),
    url(r'^api/human/$', views.HumanList.as_view()),
    url(r'^api/operator/$', views.OperatorList.as_view()),
    url(r'^api/object/$', views.ObjectList.as_view()),
    url(r'^api/rooms/$', views.RoomList.as_view(), name='name'),
]
