from django import forms
from .models import UserInfo

class NewPageForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address',]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
        }