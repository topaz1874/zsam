from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^compose/$', views.ArticleCreateView.as_view(),name='create'),
    url(r'^note_weights/$', views.AnalyticsNoteWeights.as_view(),name='note_weights'),
    url(r'^analytics/$',views.AnalyticsIndexView.as_view(),name='analytics'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.ArticleDeleteView.as_view(), name='delete'),
    url(r'^(?P<slug>[\w-]+)/update/$', views.ArticleUpdateView.as_view(), name='update'),

]