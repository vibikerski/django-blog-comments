import django_setup
from blogs.models import User, Post, Comment

user1 = User.objects.get(id=1)
user2 = User.objects.get(id=2)

post = Post.objects.get(id=1)

print(post.comment_set.all())