from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """披萨程序主页"""
    return render(request,'pizzas/index.html')

def topics(request):
    """显示所有主题"""
    topics=Pizza.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'pizzas/topics.html',context)

def topic(request,topic_id):
    """显示单个主题的所有条目"""
    pizza = Pizza.objects.get(id=topic_id) 
    toppings = pizza.topping_set.order_by('-date_added') 
    context = {'pizza': pizza, 'toppings': toppings} 
    return render(request, 'pizzas/topic.html', context) 