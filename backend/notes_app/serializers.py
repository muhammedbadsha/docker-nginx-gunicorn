from rest_framework import serializers
from .models import Notes

class NoteNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['images', 'title', 'body']
 


    def create(self, validated_data):
       
        return Notes.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.images = validated_data.get('images', instance.images)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
    