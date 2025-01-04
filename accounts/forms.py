from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# forms.py
from django import forms


# from .models import UploadedFile
from .models import UploadedFile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'title', 'description', 'visibility', 'year_published']



# class uploadBookForm(forms.ModelForm):
#     class Meta:
#         model = UploadedFile
#         fields = ['title', 'description', 'visibility', 'cost', 'year_published', 'file']

#     def clean_file(self):
#         file = self.cleaned_data.get('file')
#         if file:
#             if not (file.name.endswith('.pdf') or file.name.endswith('.jpeg') or file.name.endswith('.jpg')):
#                 raise forms.ValidationError("Only PDF and JPEG files are allowed.")
#             if file.size > 5 * 1024 * 1024:  # Restrict file size to 5MB
#                 raise forms.ValidationError("File size must be under 5MB.")
#         return file


        