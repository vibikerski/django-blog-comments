from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    date_creation = models.DateField()

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date_creation = models.DateField()

    under_post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text
