from django.shortcuts import render
from .forms import AppliationForm
from django.contrib import messages

def application(request):
    if request.method == 'POST':
        form = AppliationForm(request.POST)
        if form.is_valid():
            application=form.save(commit=False)
            application.recruiter=request.user
            application.save()
            messages.success(request, "Successfully created Application")
            return render(request, 'application/createAPP.html', {'form': AppliationForm()})
        else:
            messages.error(request, "There was an error. Please correct the form.")
    else:
        form = AppliationForm()
    return render(request, 'application/createAPP.html', {'form': form})
