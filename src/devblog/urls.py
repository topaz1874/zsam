from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetailView.as_view(), name='detail')

]