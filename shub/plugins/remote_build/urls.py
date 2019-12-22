from django.conf.urls import url, include

from shub.plugins.remote_build import views

urlpatterns = [
    url(r"v1/build$", views.BuildContainersView.as_view()),
    url(r"v1/build/(?P<buildid>.+?)?$", views.BuildContainersView.as_view()),
]
