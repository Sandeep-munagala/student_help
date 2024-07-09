from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    STUDENT_TYPE_CHOICES = [
        ('', 'Select Type'),
        ('Intermediate', 'Intermediate'),
        ('Engineering', 'Engineering'),
    ]
    
    student_type = forms.ChoiceField(label="", choices=STUDENT_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_student_type'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label="", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}), input_formats=['%d-%m-%Y'])
    college = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'}))
    year = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of Study'}), required=False)
    minor = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'minor'}))
    DEPARTMENT_CHOICES = [
        ('', 'Select Department'), 
        ('CSE', 'CSE'),
        ('CCE', 'CCE'),
        ('IT', 'IT'),
        ('ECE', 'ECE'),
        ('EEE','EEE'),
        ('ME', 'ME'),
        ('BIOTECH','BIOTECH'),
        # Add more department options here
    ]
    department = forms.ChoiceField(label="", choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'college', 'student_type', 'year', 'department','minor','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
