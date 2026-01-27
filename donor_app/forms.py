from django import forms
from .models import Donor

DISTRICT_CHOICES = [
    ('', 'Select District'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Kollam', 'Kollam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Alappuzha', 'Alappuzha'),
    ('Kottayam', 'Kottayam'),
    ('Idukki', 'Idukki'),
    ('Ernakulam', 'Ernakulam'),
    ('Thrissur', 'Thrissur'),
    ('Palakkad', 'Palakkad'),
    ('Malappuram', 'Malappuram'),
    ('Kozhikode', 'Kozhikode'),
    ('Wayanad', 'Wayanad'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
]

BLOOD_CHOICES = [
    ('', 'Select Blood Group'),
    ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), 
    ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
]

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        
        fields = ['name', 'age', 'blood_group', 'phone', 'location', 'last_donation_date']
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Full Name', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter Age', 'class': 'form-control'}),
            'blood_group': forms.Select(choices=BLOOD_CHOICES, attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}),
            'location': forms.Select(choices=DISTRICT_CHOICES, attrs={'class': 'form-control'}),
            'last_donation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }