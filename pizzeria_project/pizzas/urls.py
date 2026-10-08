"""定义 pizzas 的 URL 模式"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns=[
    # 主页
    path('',views.index,name='index'),
    # 显示所有主题的页面
    path('topics/',views.topics,name='topics'),
    # 特定主题的详细画面
    path('topics/<int:topic_id>/',views.topic,name='topic'),
]