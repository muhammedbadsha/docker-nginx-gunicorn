from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NoteNewsSerializer
from .models import Notes
from rest_framework import status
# Create your views here.

class NoteNews(APIView):
    def get(self, request, format=None):
        snippets = Notes.objects.all()
        print(snippets)
        serializer = NoteNewsSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoteNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailNotes(APIView):
    def get(self,request, pk):
        note = Notes.objects.get(pk=pk)
        # query_set = Notes.objects.filter(pk=pk)
        serializer = NoteNewsSerializer(note, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = NoteNewsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
    


