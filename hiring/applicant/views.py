from django.shortcuts import render,redirect, get_object_or_404
from .forms import ApplicationForm
from.models import Application
def application(request):
    if request.method=='POST':
        form=ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            application=form.save()
            return redirect('application_success',pk=application.pk)
    else:
        form = ApplicationForm()
    return render(request, 'hiring/application.html', {'form': form})
# Create your views here.

def application_success(request,pk):
    application=get_object_or_404(Application,pk=pk)
    return render(request, 'hiring/application_success.html', {'application': application})

def Candidates(request):
    candidates=Application.objects.all()
    return render(request,'hiring/Employer.html',{'candidates':candidates})

def Candidate_Detail(request,my_id):
    candidates=Application.objects.get(id=my_id)
    
    return render(request,'hiring/candidate_view.html',{'candidates':candidates})