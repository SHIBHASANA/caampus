from django.db import models
from django.contrib.auth.models import User


class College(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    roll_number = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png'
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


from django.db import models

# Create your models here.
