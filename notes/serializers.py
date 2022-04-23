from rest_framework import serializers

from notes.models import Note, User


# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#
#     def create(self, validated_data):
#         """ Create and return a new Note instance """
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """ Update and return an existing Note instance """
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'created_by', 'title', 'content']

