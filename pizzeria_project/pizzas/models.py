from django.db import models

class Pizza(models.Model): 
    """Defy a class of Pizza""" 
    name = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        """返回模型的字符串表示""" 
        return self.name

class Topping(models.Model): 
    """学到的有关某个主题的具体知识""" 
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE) 
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        verbose_name_plural = 'toppings' 

    def __str__(self): 
        """返回一个表示条目的简单字符串""" 
        if len(self.text)>50:
            return f"{self.text[:50]}..."
        else:
            return self.text