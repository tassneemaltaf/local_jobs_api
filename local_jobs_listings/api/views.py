from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Job, JobApplication, CustomUser

def register(request):
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      redirect('login')
  else:
    form = CustomUserForm()
  return render(request, "api/register.html", {'form': form})


def jobs_posted(request):
  user = request.user 
  jobs = Job.objects.filter(recruiter=user)
  return render(request, "api/jobs_posted.html", {'jobs': jobs, 'user': user})


def apply(request, pk):
  job = get_object_or_404(Job, pk=pk)
  if request.user.is_authenticated and request.user.role == "job_seeker":
    job.is_applied = True
    job.save() 
    return redirect('job_apps')
  return redirect('home')

class JobAppListView(generic.ListView):
  model = Job
  template_name="api/jobapplication_list.html"
  context_object_name = 'jobs'

class JobListView(generic.ListView):
  model = Job
  template_name = "api/job_list.html"
  context_object_name = 'jobs'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['user'] = self.request.user
    return context


class JobCreateView(LoginRequiredMixin, generic.CreateView):
  model = Job
  fields = ['job_title', 'location', 'job_description']
  template_name = "api/job_create.html"
  context_object_name = 'jobs'
  success_url = reverse_lazy('home')

