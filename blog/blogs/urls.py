"""定义blogs的URL模式"""

from django.urls import path

from . import views

app_name='blogs'
urlpatterns=[
    #主页
    path('',views.index,name='index'),
    #显示所有博客的页面
    path('blogs/',views.blogs,name='blogs'),
    #特定博客的详细页面
    path('blogs/<int:blog_id>/',views.blog,name='blog'),
    #添加新博客的网页
    path('new_blog/',views.new_blog,name='new_blog'),
    #添加新博文的页面
    path('new_blog_post/<int:blog_id>/',views.new_blog_post,
         name='new_blog_post'),
    #编辑已有博文的页面
    path('edit_blog_post/<int:blog_post_id>/',views.edit_blog_post,
         name='edit_blog_post'),
]