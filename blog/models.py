from django.db import models
from slugify import slugify
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=255,  null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True) 
    role = models.CharField(max_length=255, null=True, blank=True)
    skills = models.TextField(null=True, blank=True) 
    interests = models.TextField(null=True, blank=True) 
    profile_pic = models.ImageField(default="/profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def email(self):
        return self.user.email

    def __str__(self):
    	return self.name

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug
    
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS = {
        (ACTIVE, 'active'),
        (DRAFT, 'draft')
    }
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', slugify_function=slugify, unique=True)
    intro = models.TextField()
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug ,self.slug)
        

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    

    


