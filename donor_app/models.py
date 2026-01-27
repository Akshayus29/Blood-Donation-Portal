from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    DISTRICTS = [
        ('Thiruvananthapuram', 'Thiruvananthapuram'),('Kollam', 'Kollam'), ('Pathanamthitta', 'Pathanamthitta'),
        ('Alappuzha', 'Alappuzha'), ('Kottayam', 'Kottayam'), ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Palakkad', 'Palakkad'),
        ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Wayanad', 'Wayanad'),
        ('Kannur', 'Kannur'), ('Kasargod', 'Kasargod'),
    ]

    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    age = models.IntegerField(validators=[MinValueValidator(18, message="Age must be at least 18")])
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50, choices=DISTRICTS)
    last_donation_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.blood_group} - {self.location}"