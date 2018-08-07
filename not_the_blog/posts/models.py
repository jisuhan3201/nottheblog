from django.db import models
from not_the_blog.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):

    title = models.CharField(max_length=255, null=True)
    sub_title = models.CharField(max_length=255, null=True)
    intro = models.TextField(null=True)
    image = models.ImageField(null=True)
    content = models.TextField(null=True)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user, self.title)

class Comment(TimeStampedModel):

    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

class Reply(TimeStampedModel):

    content = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user, self.content)

class Star(TimeStampedModel):

    user = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stars')

    def __str__(self):
        return '{} {}'.format(self.user.username, self.post.title)
