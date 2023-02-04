from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView





urlpatterns = [
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('register/', views.register, name='register'),
    path('accounts/login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile' ),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    
    path('categories/', views.categories, name='categories'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_post/', views.new_post, name='new_post'),
    path('forbidden/', views.unauthorized_view, name='unauthorized'),

    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('my_likes/', views.my_likes, name='my_likes'),
    path('my_posts/', views.my_posts, name='my_posts'),

    path('about/', views.about, name='about'),
    
    path('like/<slug:category_slug>/<slug:slug>/', views.like_post, name='like_post'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
    
    
    
] 