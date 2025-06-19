from django.shortcuts import render
from core.decorators import login_and_role_required
# Create your views here.
@login_and_role_required("recruiter")
def dashboard(request):
    return render(request,'recruiter/dashboard.html')

