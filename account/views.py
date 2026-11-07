from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'home.html')

def admin_reg(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                return render(request,'admin_registration.html',{'error' : "Name already taken"})

            User.objects.create_superuser(
                username=username,
                password=password
            )
            return redirect('admin_login')

        return render(request,'admin_registration.html',{'error' : "Confirm password is wrong"})

    return render(request,'admin_registration.html')


def admin_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
            )


        if user is not None:

            if user.is_superuser:
                login(request,user)
                return redirect('admin_dashboard')

            return render(request,'admin_login.html',{
                'error' : "You are not authorized"
                })

        return render(request,'admin_login.html',{
            'error' : "Invalid Username or Password"
        })

    return render(request,'admin_login.html')



@login_required(login_url='admin_login')
@never_cache
def admin_dashboard(request):

    if request.user.is_superuser:
        return render(request,'admin_dashboard.html')

    return redirect('admin_login')


@login_required(login_url='admin_login')
@never_cache
def admin_logout(request):
    logout(request)
    # request.session.flush()
    return redirect('admin_login')



def admin_session(request):

    request.session['username'] = 'albin'

    name = request.session.get('username')

    exists = 'username' in request.session

    return render(request,'session.html',{
        'name' : name,
        'exists' : exists
    })