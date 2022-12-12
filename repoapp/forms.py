from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=10)
    last_name =forms. CharField(label='Apellido', max_length=10)
    edad = forms.CharField(max_length=2)
    username = forms.CharField(label='Nombre de usuario',max_length=10)
    password1 = forms.CharField(label='Contraseña',max_length=15, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña',max_length=15,widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','edad','username','password1','password2']
        help_texts = {k:"" for k in fields}







    


