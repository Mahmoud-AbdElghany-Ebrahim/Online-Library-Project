from django import forms
from .models import Student

class update(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'Fname',
            'Lname',
            'email',
            'password',
            'phoneNum',
            'Bdate',
            'Gender',
            'User',
        ]