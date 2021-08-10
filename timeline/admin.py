from django.contrib import admin

from timeline.posts.models import Post
from timeline.comments.models import Comment
from timeline.users.models import UserProfile


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
