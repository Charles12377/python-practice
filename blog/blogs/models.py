from django.db import models

# Create your models here.
class Blog(models.Model):
    """博客模型"""
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Blog_post(models.Model):
    """某个博客下的博文"""
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='blog_posts'

    def __str__(self):
        return f"{self.text[:50]}..."