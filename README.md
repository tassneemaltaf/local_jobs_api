# Local Jobs Listings API

## Overview
The Local Jobs Listings API is a platform that helps unemployed individuals find local job opportunities while allowing recruiters to post job openings. 
The project is live on: https://tassneemaltaf.pythonanywhere.com/ until June of 2025

## Objective
Help unemployed individuals find local job opportunities.

## Features

### Job Seeker Features:
- View and search for job listings.
- Apply for jobs.

### Job Recruiter Features:
- Post job opportunities.
- Delete job opportunities


### Additional Features:
- **Application Status**: Recruiters can mark applications as "Pending", "Reviewed", "Accepted", or "Rejected".

## Technologies Used
- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For API development.
- **SQLite**: Database for storing user and job data.
- **JWT**: For user authentication.

## Getting Started

### Prerequisites
To run this project locally, you need:
- Python 3.11
- pip (Python package installer)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/tassneemaltaf/local-jobs-api.git
   cd local-jobs-api
2. **Create and activate a virtual environment**:
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install Dependencies**:
   pip install -r requirements.txt

4. **Run migrations**:
   python manage.py migrate

5. **Create a Super User for Admin Access**:
   python manage.py createsuperuser

6. **Run the development server**:
   python manage.py runserver

Your API should now be running at http://127.0.0.1:8000/.

**API Endpoints**
- POST /register/
  Register a new user
  
- POST /login/
  Login user

- GET /accounts/profile/
  User profile
  
- GET /jobs_posted/
  Get jobs posted (only for recruiter)
  
 - GET /
   Get Job listing

- POST /new/
  Create new job (Only for recruiters)

- POST delete/{id}/
  Delete a job (Only for recruiters)

- GET /job_apps/
  Get all the jobs the current logged in applicant applied for

- POST /apply/{id}/
  Apply for a job
  


