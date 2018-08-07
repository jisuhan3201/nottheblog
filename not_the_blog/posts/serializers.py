from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    comment = CommentSerializer()

    class Meta:
        model = models.Reply
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Star
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    stars = StarSerializer(many=True)

    class Meta:
        model = models.Post
        fields = (
            "title",
            "sub_title",
            "intro",
            "image",
            "content",
            "user",
            "comments",
            "stars",
        )
