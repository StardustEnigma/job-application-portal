from .models import Application
from django import forms

Gender_choices=(
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

JOB_CITY_CHOICES = [
    ("Nagpur", "Nagpur"),
    ("Mumbai", "Mumbai"),
    ("Pune", "Pune"),
    ("Bangalore", "Bangalore"),
    ("Hyderabad", "Hyderabad"),
    ("Delhi", "Delhi"),
    ("Chennai", "Chennai"),
    ("Ahmedabad", "Ahmedabad"),
]

class ApplicationForm(forms.ModelForm):
    gender=forms.ChoiceField(
        choices=Gender_choices,
        widget=forms.RadioSelect
    )
    job_city=forms.MultipleChoiceField(
         choices=JOB_CITY_CHOICES,
         widget=forms.CheckboxSelectMultiple

         )
    class Meta:
        model =Application
        fields = ('name','dob','gender','locality','city','pin','state','email','job_city','profile_pic','resume')
        labels = {
    'name': 'Full Name',
    'dob': 'Date of Birth',
    'gender': 'Gender',
    'locality': 'Local Address / Locality',
    'city': 'City',
    'pin': 'Pin Code',
    'state': 'State',
    'email': 'Email Address',
    'job_city': 'Preferred Job City',
    'profile_pic': 'Profile Picture',
    'resume': 'Resume (PDF, DOCX)',
}   
        
        help_texts = {
    'profile_pic': 'Upload a clear, recent photo (JPG, PNG).',
    'resume': 'Upload your latest resume (PDF or DOCX).',
}
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'dob': forms.DateInput(attrs={'type': 'date','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'placeholder':'Write your address here'}),
            'city':forms.TextInput(attrs={'placeholder':'City'}),
            'pin':forms.NumberInput(attrs={'placeholder':'Enter 6 Digit pin code'}),
            'state':forms.Select(attrs={'placeholder':'Enter State'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter Email Address'})

}