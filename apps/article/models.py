from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=10,verbose_name="标题")
    author = models.CharField(max_length=10,verbose_name="作者")
    add_time  = models.DateTimeField(verbose_name="添加时间")
    body = models.TextField(max_length=500,verbose_name="文章")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title