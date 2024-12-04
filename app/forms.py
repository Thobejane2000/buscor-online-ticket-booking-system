from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# SignUpForm for user registration
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )
    name = forms.CharField(max_length=30, label="Name")
    surname = forms.CharField(max_length=30, label="Surname")
    id_number = forms.CharField(max_length=20, label="ID Number")
    phone = forms.CharField(max_length=15, label="Phone Number")

    class Meta:
        model = User
        fields = ('username',)
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# MessageFilterForm for filtering messages
class MessageFilterForm(forms.Form):
    MESSAGE_TYPE_CHOICES = [
        ('', 'All'),
        ('booking', 'Booking Confirmation'),
        ('promotion', 'Promotional Offer'),
        ('service', 'Service Alert'),
        ('support', 'Customer Support'),
        ('feedback', 'Feedback Request'),
        ('general', 'General Announcement'),
    ]
    
    message_type = forms.ChoiceField(choices=MESSAGE_TYPE_CHOICES, required=False)
    search = forms.CharField(max_length=100, required=False)
