from django.urls import path
from . import views




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile' ),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    
    path('categories/', views.categories, name='categories'),
    path('new_post/', views.new_post, name='new_post'),
    path('forbidden/', views.unauthorized_view, name='unauthorized'),

    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('about/', views.about, name='about'),
    
    path('like/<slug:category_slug>/<slug:slug>/', views.like_post, name='like_post'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    
    
    
] 