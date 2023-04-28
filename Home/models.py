from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    address = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    last_upd = models.DateTimeField(
        default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        db_table = 'userprofiles'


class UserReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_id = models.BigAutoField(auto_created=True, primary_key=True)
    age = models.PositiveIntegerField()
    t3 = models.DecimalField(max_digits=5, decimal_places=2)
    tt4 = models.DecimalField(max_digits=5, decimal_places=2)
    t4u = models.DecimalField(max_digits=5, decimal_places=2)
    fti = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.IntegerField()
    sick = models.IntegerField()
    pregnant = models.IntegerField()
    thyroid_surgery = models.IntegerField()
    goitre = models.IntegerField()
    tumor = models.IntegerField()
    category = models.CharField(max_length=20, null=True)

    upload_date = models.DateTimeField(
        default=datetime.datetime.now(), blank=True)

    class Meta:
        db_table = 'patients'

    def __str__(self):
        return self.user.username


class Appointments(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='doctor')
    # doctor_id = models.BigAutoField(auto_created=True, primary_key=True)
    # Add additional fields for the Doctor model
    specialty = models.CharField(max_length=100)
    bio = models.TextField()

    class Meta:
        db_table = 'doctor'
