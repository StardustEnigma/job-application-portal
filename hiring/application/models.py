from django.db import models
from django.contrib.auth import get_user_model

user=get_user_model()


class CreateApplication(models.Model):
    recruiter = models.ForeignKey(user, on_delete=models.CASCADE)  # Link to recruiter

    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()

    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)  # Add job_type field
    salary_range = models.CharField(max_length=100)

    openings = models.IntegerField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
