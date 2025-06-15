from django.shortcuts import render,redirect
from .forms import registerationForm
from django.contrib import messages

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
            messages.success(request,'Registeration Successfull please check your email for to activate account')
            return redirect('login')
        else:
            # This will show errors in template
            return render(request, 'account/register.html', {'form': form})
    else:
        form=registerationForm()

    return render(request,'account/register.html',{'form':form})


