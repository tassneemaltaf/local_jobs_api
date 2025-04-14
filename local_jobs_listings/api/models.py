from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

#Creating a Custom user model
class CustomUserManager(UserManager):
  def _create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError("You have not provided a valid e-mail address")

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)
  
  def create_superuser(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self._create_user(email, password, **extra_fields)

#Custom User has attributes like name, email, role, password and profile_picture. The role attribute has 
class CustomUser(AbstractBaseUser, PermissionsMixin):
  JOB_SEEKER = "job_seeker"
  RECRUITER = "recruiter"

  ROLE_CHOICES = [
    (JOB_SEEKER, "Job Seeker"),
    (RECRUITER, 'Recruiter'),
  ]

  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=JOB_SEEKER)
  profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'role']

#Job seeker model has a foreign key to the custom user id, age, nationality and skills attributes
class JobSeeker(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  age = models.IntegerField()
  nationality = models.CharField(max_length=255)
  skills = models.TextField()

#This is the Job Role model, that has attributes such as: title, location, description and recruiter_id
class Job(models.Model):
  job_title = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  job_description = models.TextField()
  is_applied = models.BooleanField(default=False)
  recruiter = models.ForeignKey(
    CustomUser,
    on_delete=models.CASCADE,
    related_name="jobs"
  )

#This model is to check the job application process for a certain job role
class JobApplication(models.Model):
  APPLIED = "applied"
  NOT_APPLIED = "not_applied"

  STATUS_CHOICES = [
    (APPLIED, "Applied"),
    (NOT_APPLIED, "Not Applied"),
  ]

  job_id = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job")
  applicant_id = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name="applicant")
  application_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_APPLIED)


