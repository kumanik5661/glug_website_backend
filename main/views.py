from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from main.models import Event, Profile, About, Project
from main import serializers

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer
    lookup_field = 'identifier'
    http_method_names = ['get']

event_list = EventViewSet.as_view({
    'get':'list'
})

event_detail = EventViewSet.as_view({
    'get': 'retrieve'
})


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    http_method_names = ['get']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = serializers.AboutSerializer
    lookup_field = 'identifier'
    http_method_names = ['get']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializers
    lookup_field = 'identifier'
    http_method_names = ['get']