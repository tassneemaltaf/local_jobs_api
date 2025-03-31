from django.contrib import admin
from .models import CustomUser, JobSeeker, Job, JobApplication

admin.site.register(CustomUser)
admin.site.register(JobSeeker)
admin.site.register(Job)
admin.site.register(JobApplication)

