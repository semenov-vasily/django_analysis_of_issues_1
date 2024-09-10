from django.contrib.auth.models import User
from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)  # название модели в кавычках если она ниже в коде
    is_main = models.BooleanField(default=False)  # основной тег



class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, through=PostTag)  # при связи м2м указываем промежуточную таблицу through=PostTag


    def __str__(self):
        return self.title


# category_obj = Category.objects.get(id=1)  # получение записи id=1 из таблицы Category
# Post.objects.filter(category=category_obj)  # получение записей из таблицы Post у которых поле category = category_obj
# category_obj.posts.all()  # делает аналогично предыдущему, для этого нужно related_name="posts"

