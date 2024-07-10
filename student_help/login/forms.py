from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import College  # Import your College model here

class EngineeringSignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label="", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}), input_formats=['%d-%m-%Y'])
    
    # Define the college field with a ChoiceField
    college = forms.ChoiceField(
        label="",
        choices=[],  # Choices will be dynamically updated in __init__
        widget=forms.Select(attrs={'class': 'form-control select-college', 'id': 'id_college'}),  # Add id attribute for JavaScript
        required=False  # Set to False to allow for the "Others" option
    )

    # Additional field for entering college name when selecting "Others"
    other_college = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter College Name', 'style': 'display: none;'}),  # Initially hidden
        required=False
    )

    year = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of Study'}))
    minor = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minor'}))
    
    DEPARTMENT_CHOICES = [
        ('', 'Select Department'), 
        ('Computer Science', 'Computer Science'),
        ('Electrical and Communication', 'Electrical and Communication'),
        ('Mechanical', 'Mechanical'),
        ('Civil', 'Civil'),
        ('Chemical', 'Chemical'),
        ('Others', 'Others'),
    ]
    department = forms.ChoiceField(label="", choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'college', 'other_college', 'year', 'department', 'minor', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(EngineeringSignUpForm, self).__init__(*args, **kwargs)
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

        # Populate choices for the college field
        self.fields['college'].choices = self.get_college_choices()

        # Add JavaScript class to the widget
        self.fields['college'].widget.attrs['class'] = 'form-control select-college'

    def get_college_choices(self):
        """Return choices for the college dropdown including 'Others'."""
        choices = [('','Select College')]  # Initial empty choice
        colleges = College.objects.all()  # Replace with actual queryset
        for college in colleges:
            choices.append((college.name, college.name))
        choices.append(('Others', 'Others'))  # Add 'Others' option
        return choices

class IntermediateSignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label="", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD-MM-YYYY'}), input_formats=['%d-%m-%Y'])
    college = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'college', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(IntermediateSignUpForm, self).__init__(*args, **kwargs)
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