from django.conf.urls import url
from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("all/", view=views.ListAllPosts.as_view(), name='all_posts'),
    path("comments/", view=views.ListAllComments.as_view(), name='all_comments'),
    path("replies/", view=views.ListAllReplies.as_view(), name='all_replies'),
    path("stars/", view=views.ListAllStars.as_view(), name='all_stars'),
]
