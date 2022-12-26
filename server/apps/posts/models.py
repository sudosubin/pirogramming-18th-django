from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    user = models.CharField(max_length=50, verbose_name="사용자 이름")
    content = models.TextField(verbose_name="내용")
    region = models.CharField(max_length=50, verbose_name="지역")
    price = models.IntegerField(verbose_name="가격")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "post"
        verbose_name = "게시글"
