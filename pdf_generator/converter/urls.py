"""The module to which the url path of the category application are located."""

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.FileUploadView.as_view()),
]
