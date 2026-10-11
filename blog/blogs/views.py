from django.shortcuts import render,redirect

from .models import Blog,Blog_post
from .forms import BlogForm,Blog_postForm
# Create your views here.
def index(request):
    """播客主页"""
    return render(request,'blogs/index.html')

def blogs(request):
    """显示所有博客"""
    blogs=Blog.objects.order_by('date_added')
    context={'blogs':blogs}
    return render(request,'blogs/blogs.html',context)

def blog(request,blog_id):
    """显示单个博客及其所有博文"""
    blog=Blog.objects.get(id=blog_id)
    blog_posts=blog.blog_post_set.order_by('-date_added')
    context={'blog':blog,'blog_posts':blog_posts}
    return render(request,'blogs/blog.html',context)

def new_blog(request):
    """添加新博客"""
    if request.method != 'POST':
        #未提交数据：对数据进行处理
        form=BlogForm()
    else:
        #POST提交的数据：对数据进行处理
        form=BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    #显示空表单或指出表单数据无效
    context={'form':form}
    return render(request,'blogs/new_blog.html',context)

def new_blog_post(request,blog_id):
    """在特定博客中添加新博文"""
    blog=Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        #未提交数据：创建一个空表单
        form=Blog_postForm()
    else:
        #POST提交的数据：对数据进行处理
        form=Blog_postForm(data=request.POST)
        if form.is_valid():
            new_blog_post=form.save(commit=False)
            new_blog_post.blog=blog
            new_blog_post.save()
            return redirect('blogs:blog',blog_id=blog_id)

    #显示空表单或指出表单数据无效
    context={'blog':blog,'form':form}
    return render(request,'blogs/new_blog_post.html',context)

def edit_blog_post(request,blog_post_id):
    blog_post=Blog_post.objects.get(id=blog_post_id)
    blog=blog_post.blog

    if request.method != 'POST':
        # 初次请求：使用当前的条目填充表单
        form = Blog_postForm(instance=blog_post) 
    else: 
        # POST 提交的数据：对数据进行处理
        form = Blog_postForm(instance=blog_post, data=request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('blogs:blog', blog_id=blog.id) 
 
    context = {'blog_post': blog_post, 'blog': blog, 'form': form} 
    return render(request, 'blogs/edit_blog_post.html', context)