from django.http import HttpResponse
from django.shortcuts import redirect, render
from blog.models import Category

categories_all = Category.objects.all()


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group= None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
                
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
        if group == 'staff':
            return view_func(request, *args, **kwargs)
        
        else:
            return render(request, 'registration/unauthorized_page.html',{'categories':categories_all})
    
    return wrapper_func
