from django.shortcuts import render
from .forms import CustomUserForm
from django.views import generic
from django.urls import reverse_lazy

class RegisterView(generic.CreateView):
  form_class = CustomUserForm
  success_url = reverse_lazy("login")
  template_name = "api/register.html"