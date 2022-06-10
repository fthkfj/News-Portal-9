from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        leaders_rating = Post.objects.filter(postAuthor=self).values('leadersRating')
        leaders_rating = sum(p['leadersRating'] for p in leaders_rating) * 3
        leaders_comment = Comment.objects.filter(commentAuthor=self).values('ledersComment')
        leaders_comment = sum(c['leadersComment'] for c in leaders_comment)
        rating = leaders_rating + leaders_comment
        return rating


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def get_email(self):
        result = set()
        for users in self.subscribers.all():
            result.add(users.email)
        return result


class Post(models.Model):
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'nw'
    ARTICLE = 'ar'
    SELECT = (
        (NEWS, 'Новости'),
        (ARTICLE, 'Статья')
    )
    CategoryType = models.CharField(max_length=50, choices=SELECT, default=ARTICLE)
    DateCreation = models.DateTimeField(auto_now_add=True)
    PostCategories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    ratings = models.IntegerField(default=0)

    def like(self):
        self.ratings += 1

    def dislike(self):
        self.ratings -= 1

    def preview(self):
        return self.text[0:124] + '...'


class PostCategory(models.Model):
    PostTrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    CategoryTrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    CommentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    DateCreation = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField(default=0)

    def like(self):
        self.ratings += 1
        self.save()

    def dislike(self):
        self.ratings -= 1
        self.save()
















