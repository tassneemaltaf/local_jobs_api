from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Job

class CustomUserForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['name', 'email', 'role', 'profile_picture']
  def save(self, commit=True):
    job = super().save(commit=False)
    job.recruiter = self.user 
    if commit:
      job.save()
    return job