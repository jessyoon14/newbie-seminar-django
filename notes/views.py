from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """ viewset automatically provides list, create, retrieve, update, and destroy"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
