from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ValidationError
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['email'].widget.attrs['required'] = True
        self.fields['password1'].widget.attrs['placeholder'] = self.fields['password1'].label
        self.fields['password2'].widget.attrs['placeholder'] = self.fields['password2'].label

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count() > 0:
            raise ValidationError("Esta dirección de email ya esta en uso.")
        return data

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label
        self.fields['password'].widget.attrs['placeholder'] = self.fields['password'].label
