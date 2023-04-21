from django import forms
from appTwo.models import Users

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Users
        field = '__all__'