# Local Jobs Listings API

## Overview
A Django REST API for job seekers and recruiters to manage job listings and applications. Built with Django Rest Framework (DRF) and JWT authentication.

🚀 Features
User registration with role: job_seeker or recruiter

JWT-based login and authentication

Recruiters can:

Post, update, delete job listings

View all their job posts

Job seekers can:

Apply to jobs

View their applications

Secure access to views based on user role

🔐 Authentication
JWT authentication via rest_framework_simplejwt

Use /api/token/ to get access + refresh tokens

Include your token in requests using:
Authorization: Bearer <access_token>

🔧 API Endpoints

Auth
Method	Endpoint	Description
POST	/register/	Register new user
POST	/api/token/	Get JWT tokens
POST	/api/token/refresh/	Refresh access token

Jobs
Method	Endpoint	Description
GET	/api/jobs/	List all jobs
GET	/api/jobs/<id>/	Get job details
POST	/jobs/create/	Create a job post (recruiter)
PUT	/jobs/update/<id>/	Update job post (recruiter)
DELETE	/jobs/delete/<id>/	Delete job post (recruiter)

Applications
Method	Endpoint	Description
POST	/jobs/<id>/apply/	Apply to a job (job seeker only)
GET	/my-applications/	View all your applications
GET	/my-jobs/	View jobs posted by you (recruiter)


🛠️ Setup Instructions

Clone the project
git clone <your-repo-url>
cd local_jobs_listings

Create and activate a virtual environment
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate

Install dependencies
pip install -r requirements.txt


Run migrations
python manage.py makemigrations
python manage.py migrate

Start the server
python manage.py runserver


📦 Dependencies
Django
Django REST Framework
djangorestframework-simplejwt
