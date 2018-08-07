from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllPosts(APIView):

    def get(self, request, format=None):


        all_posts = models.Post.objects.all()

        serializer = serializers.PostSerializer(all_posts, many=True)

        return Response(data=serializer.data)


class ListAllComments(APIView):

    def get(self, request, format=None):


        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllReplies(APIView):

    def get(self, request, format=None):


        all_replies = models.Reply.objects.all()

        serializer = serializers.ReplySerializer(all_replies, many=True)

        return Response(data=serializer.data)


class ListAllStars(APIView):

    def get(self, request, format=None):


        all_stars = models.Star.objects.all()

        serializer = serializers.StarSerializer(all_stars, many=True)

        return Response(data=serializer.data)
