from django.urls import path

from . import views

urlpatterns = [
    # ex: /meals/
    path("", views.index, name="index"),
    # ex: /meals/5/
    path("<int:id>/", views.detail, name="detail"),
    # ex: /meals/week/5/
    path("week/<int:id>/", views.week, name="week"),
    # ex: /meals/5/vote/
    path("<int:id>/vote/", views.vote, name="vote"),
]