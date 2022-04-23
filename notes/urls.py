from django.urls import path
from notes import views
from notes.views import NoteViewSet

note_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

note_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('notes/', note_list, name='note-list'),
    path('notes/<int:pk>/', note_detail, name='note-detail'),
]

