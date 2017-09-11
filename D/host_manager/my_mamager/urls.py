from django.conf.urls import url
from my_mamager import views
urlpatterns = [
    url(r'^show_manager/(?P<id>\d+)', views.show_manager),
    url(r'^modify', views.modify),
    url(r'^delete', views.delete),
    url(r'^add', views.add),
    url(r'^search', views.search),
    url(r'^check_host', views.check_host),
    url(r'^check_service', views.check_service),
    url(r'^service', views.add_service),
    # url(r'^p_add', views.p_add),
]
