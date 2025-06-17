from django.shortcuts import render,redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def dashboard(request):
    return render(request,'user/dashboard.html')
@login_required
def password_change_view(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            logout(request)
            messages.success(request,"Password change successfully please login with your new password")
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'user/password_change.html')