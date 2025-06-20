from django import forms
from .models import CreateApplication

LOCATION_CHOICES = [
    ("Remote", "Remote"),
    ("Hybrid", "Hybrid"),
    ("On-Site", "On-Site"),
]

JOB_TYPE_CHOICES = [
    ("Internship", "Internship"),
    ("Part-Time", "Part-Time"),
    ("Full-Time", "Full-Time"),
]

class AppliationForm(forms.ModelForm):
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.RadioSelect
    )

    job_type = forms.ChoiceField(
        choices=JOB_TYPE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = CreateApplication
        exclude = ['recruiter']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
