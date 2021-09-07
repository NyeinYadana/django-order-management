from django.shortcuts import redirect
from django.http.response import HttpResponse
def authenticated_user(view_func):
    def wrapper(request):  #func wraper
        if not request.user.is_authenticated:
            return view_func(request)
        else:
            return redirect('/')
    return wrapper;

def admin_only(view_func):
    def wrapper(request):
        if request.user.groups.first().name=='admin':
            return view_func(request)
        if request.user.groups.first().name=='customer':
            return redirect('/customer_profile')
    return wrapper;

#======================================
#      Allowed Roles with 3 layers func
#======================================
def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper(request,*args, **kwargs):  #**all arguments, **keywordarguments
            if request.user.groups.first().name in roles:
                return view_func(request,*args, **kwargs)  #order create
            else:
                return HttpResponse('You are not authorized')
        return wrapper;
    return decorator;

