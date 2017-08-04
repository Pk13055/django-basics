from django.conf.urls import url 
from . import views

app_name = "polls"
urlpatterns = [
	url(r'^(?P<number>[0-9]+)/(?P<name>([A-Z]|[a-z])+)/$', views.index, name = "index"),
	url(r'^form/$', views.form, name = "form"),
	url(r'^form/(?P<pk>\d+)/$', views.Detail.as_view()	, name = "listView")
]