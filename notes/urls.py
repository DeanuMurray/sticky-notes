from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.NoteListView.as_view(), name="list"),
    path("add/", views.NoteCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", views.NoteUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="delete"),
]
