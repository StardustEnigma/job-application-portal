from django.db import models
from django.core.exceptions import ValidationError

def Validate_pin(value):
    if len(str(value)) != 6:
        raise ValidationError('The pin must of 6 digit')
    
STATE_CHOICES = [
    ("AN", "Andaman and Nicobar Islands"),
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CH", "Chandigarh"),
    ("CT", "Chhattisgarh"),
    ("DN", "Dadra and Nagar Haveli and Daman and Diu"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("LA", "Ladakh"),
    ("LD", "Lakshadweep"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OD", "Odisha"),
    ("PY", "Puducherry"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TS", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal")
]

# Create your models here.
class Application(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=1)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveBigIntegerField(validators=[Validate_pin],help_text="Enter 6 digit pin code")
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    email=models.EmailField(null=True,blank=True)
    job_city = models.JSONField(default=list)
    profile_pic=models.ImageField(upload_to='profileimg',blank=True)
    resume=models.FileField(upload_to='resume', blank=True)
    
class Interview(models.Model):
    candidate=models.ForeignKey(Application,on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    platform_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending') 
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)