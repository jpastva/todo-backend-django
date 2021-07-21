from django.urls import path, re_path

from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from todo_backend_django import views

urlpatterns = [
    path('', RedirectView.as_view(url='/todos')),
    re_path(r'^$', RedirectView.as_view(url='/todos')),
    re_path(r'^todos$', views.TodoList.as_view()),
    re_path(r'^todo/(?P<pk>[0-9]+)$', views.Todo.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
