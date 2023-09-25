from django.urls import path
from .import views
urlpatterns = [
    path('',views.NoteNews.as_view(),name='note_news'),
    path('<int:pk>',views.DetailNotes.as_view(),name='note_detail'),

]
