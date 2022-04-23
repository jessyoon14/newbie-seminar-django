from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from notes.models import Note, User
from notes.serializers import NoteSerializer, UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """ viewset automatically provides list, create, retrieve, update, and destroy"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data['title'].upper()
        serializer.save(title=title)


class UserViewSet(viewsets.ModelViewSet):
    """ viewset automatically provides list, create, retrieve, update, and destroy"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
