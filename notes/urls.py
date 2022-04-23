from django.urls import path
from notes.views import NoteViewSet, UserViewSet

note_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

note_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('notes/', note_list, name='note-list'),
    path('notes/<int:pk>/', note_detail, name='note-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
]

