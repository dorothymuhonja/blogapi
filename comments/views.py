from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
# from rest_framework import generics, permissions
from .models import *
from .serializers import *
# from .permissions import IsAuthorOrReadOnly



class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
