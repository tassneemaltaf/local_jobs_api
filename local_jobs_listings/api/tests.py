from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser
import json

class JobTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(name="Anissa", email="Anissa@gmail.com", role="recruiter")
        self.user.set_password("Testpass")  # Hash password properly
        self.user.save()
        self.client.force_login(self.user)
        super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_list_job(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #This test will fail if we dont remove LoginRequiredMixin to test this
    def test_create_job(self):
        data = {"job_title": "Software Engineer", "location": "Eindhoven", "job_description": "Full time", "recruiter": self.user.id}
        url = reverse('job_create')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




