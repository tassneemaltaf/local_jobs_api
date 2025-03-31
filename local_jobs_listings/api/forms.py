from django.forms import ModelForm
from .models import CustomUser, Job

class CustomUserForm(ModelForm):
  class Meta:
    model = CustomUser
    fields = ['name', 'email', 'role', 'password', 'profile_picture']


class JobForm(ModelForm):
  class Meta:
    model = Job
    fields = ['job_title', 'location', 'description']