from django.shortcuts import render,redirect
from .forms import registerationForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from .utils import send_activation_email
from .models import User
def login(request):
    return render(request,'account/login.html')


def register_view(request):
    if request.method=="POST":
        form=registerationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            user.save()
            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            token=default_token_generator.make_token(user)
            activation_link=reverse('activate',kwargs={'uidb64':uidb64,'token':token})
            activation_url=f'{settings.SITE_DOMAIN}{activation_link}'
            send_activation_email(user.email,activation_url)
            messages.success(request,'Registeration Successfull please check your email for to activate account')
            return redirect('login')
        else:
            # This will show errors in template
            return render(request, 'account/register.html', {'form': form})
    else:
        form=registerationForm()

    return render(request,'account/register.html',{'form':form})

def activate_account(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request,"This account has already been activated")
            return redirect('login')
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,'Your account has been activated successfully')
            return redirect('login')
        else:
            messages.error(request,"The activation link is invalid or expired")
            return redirect('login')
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(request,"Invalid activation link")
        return redirect('login')