from django.db import models
from django.contrib.auth.models import User
# from django.db.models import Max

# Create your models here.


class LocalUser(User):
    pass


class Author(models.Model):
    _author_rating = models.IntegerField(default=0, db_column='author_rating')
    author_user = models.OneToOneField(LocalUser, on_delete=models.CASCADE)

    def update_rating_author(self):
        self._author_rating = 0
        for post in self.post_set.all():
            self._author_rating += post._post_rating * 3
        for other_comm in post.comment_set.exclude(user__username=self.author_user.username):
            self._author_rating += other_comm._comment_rating
        for comment in self.author_user.comment_set.all():
            self._author_rating += comment._comment_rating
        self.save()


class Category(models.Model):

    name_category = models.CharField(max_length=100, unique=True, blank=False)


class Post(models.Model):
    news = 'NS'
    article = 'AC'
    NEWS_ARTICLE = (
        (news, 'Новость'),
        (article, 'Статья')
    )
    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    post_type = models.CharField(choices=NEWS_ARTICLE, default='NS', max_length=2)
    post_creation = models.DateTimeField(auto_now_add=True)
    _post_rating = models.IntegerField(default=0, db_column='post_rating')
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self._post_rating += 1
        self.save()

    def dislike(self):
        self._post_rating -= 1
        self.save()

    def preview_post(self):
        return f'{self.post_text[:123]}...'


class Comment(models.Model):

    comment_text = models.CharField(max_length=255, default='Empty')
    comment_creation = models.DateTimeField(auto_now_add=True)
    _comment_rating = models.IntegerField(default=0, db_column='comment_rating')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self._comment_rating += 1
        self.save()

    def dislike(self):
        self._comment_rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
