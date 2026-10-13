from django.db import models
from django.http import Http404

from django.contrib.auth.models import User 

class Topic(models.Model): 
    """用户学习的主题""" 
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def check_topic_owner(self, request_user):
        """确认主题属于当前登录用户"""
        if self.owner != request_user: 
            raise Http404
    
    def __str__(self):  
        """返回模型的字符串表示""" 
        return self.text

class Entry(models.Model): 
    """学到的有关某个主题的具体知识""" 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        verbose_name_plural = 'entries' 

    def __str__(self): 
        """返回一个表示条目的简单字符串""" 
        if len(self.text)>50:
            return f"{self.text[:50]}..."
        else:
            return self.text

        