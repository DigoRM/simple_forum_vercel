from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment, Category, Customer
from django.contrib.auth.models import User

from blog.forms import CommentForm, CreateUserForm, PostForm, CustomerForm, ProfileImageForm, UserUpdateForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .decorators import admin_only
from django.db.models import Count



categories_all = Category.objects.all()

# Create your views here.

def home(request):
    posts = Post.objects.filter(status = Post.ACTIVE).annotate(num_comments=Count('comments'), num_likes=Count('likes')).order_by('-created_at')
    user=request.user
    

    
    return render(request, 'blog/home.html', {'posts':posts, 'categories':categories_all,'authors': [post.author.customer for post in posts]})

def most_liked(request):
    posts = Post.objects.filter(status = Post.ACTIVE).annotate(num_comments=Count('comments'), num_likes=Count('likes')).order_by('-num_likes')


    
    return render(request, 'blog/most_liked.html', {'posts':posts, 'categories':categories_all,'authors': [post.author.customer for post in posts]})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).annotate(num_comments=Count('comments'), num_likes=Count('likes')).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts, 'categories':categories_all, 'authors': [post.author.customer for post in posts]})

@login_required
def my_likes(request):
    posts = Post.objects.filter(likes__in=[request.user]).annotate(num_comments=Count('comments'), num_likes=Count('likes')).order_by('-created_at')
    return render(request, 'blog/my_likes.html', {'posts': posts, 'categories':categories_all, 'authors': [post.author.customer for post in posts]})

@login_required
def new_post(request):
    user = request.user    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           
           return redirect('/')
    else:
        form = PostForm()
        
    return render(request, 'blog/new_post.html', {'form':form, 'categories':categories_all, 'user':user})

def categories(request):
    categories = Category.objects.all().prefetch_related(Prefetch('posts', queryset=Post.objects.filter(status='active')))
    return render(request, 'blog/categories.html', {'categories':categories})

def about(request):
    return render(request, 'blog/about.html', {'categories':categories_all})

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)
    user = request.user
    users_who_liked_post = post.likes.all()
    user_liked = request.user in users_who_liked_post
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        user = request.user
        if form.is_valid():
           comment = form.save(commit=False)
           comment.author = request.user
           comment.post = post
           comment.save()
           
           return redirect('post_detail',category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/detail.html', {'post':post, 'form':form, 'categories':categories_all, 'user':user,'users_who_liked_post':users_who_liked_post,'user_liked':user_liked})


def like_post(request, slug, category_slug):
    post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail',category_slug=category_slug, slug=slug)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status = Post.ACTIVE).annotate(num_comments=Count('comments')).order_by('-created_at')
    return render(request, 'blog/category.html', {'category':category, 'posts':posts, 'categories':categories_all,'authors': [post.author.customer for post in posts]})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains = query) | Q(intro__icontains=query) | Q(body__icontains = query))
    
    return render(request, 'blog/search.html', {'posts':posts , 'query':query, 'categories':categories_all})

def robots_txt(request):
    text=[
        "User-Agent: *",
        "Disallow: /admin/",
          ]
    return HttpResponse('\n'.join(text), content_type="text/plain")

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context={}
    return render(request, 'registration/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('login')       


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')


                messages.success(request, "Welcome " + username + "!")
                
                
                return redirect('login')
        
        
        context = {'form':form}
        return render(request, 'registration/register.html', context)
    

@login_required(login_url='login')
def profile(request):
    user = request.user
    customer = user.customer
    email = customer.email()
    form = CustomerForm(instance=customer)
    form_image = ProfileImageForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        form_image = ProfileImageForm(request.POST, request.FILES,instance=customer)
        if form.is_valid() and form_image.is_valid():
            form.save()
            
    context = {'form':form,
               'categories':categories_all,
               'customer':customer,
               'email':email,
               'form_image':form_image
               }
    return render(request, 'registration/profile.html', context)

@login_required(login_url='login')
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    customer = user.customer
    context = {
        'customer': customer,
        'user':user,
    }
    return render(request, 'registration/user_profile.html', context)

def unauthorized_view(request):
    user = request.user
    context={
        'user':user,
        'categories':categories_all
    }
    return render(request, 'registration/unauthorized_page.html',context)

@login_required
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/update_user.html', {'form': form})
