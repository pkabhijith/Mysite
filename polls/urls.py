from django.conf.urls import url

from . import views

app_name='polls'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #e.x: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    #e.x: /polls/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    #e.x: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote')

    url(r'^$', views.IndexView.as_view(), name='index'),
    # e.x: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # e.x: /polls/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # e.x: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]