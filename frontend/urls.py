from django.urls import path
from . import views

urlpatterns = [
    path("", views.FrontEndRendererView.as_view(), name="frontend-index"),
    path("logged_in/", views.FrontEndRendererView.as_view(), name="frontend-logged-in"),
    path("home/", views.FrontEndRendererView.as_view(), name="frontend-home"),
    path("problems/", views.FrontEndRendererView.as_view(), name="frontend-problem-list"),
]
