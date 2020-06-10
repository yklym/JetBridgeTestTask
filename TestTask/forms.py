from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ViralUser


class RegisterForm(UserCreationForm):
    ref_code = forms.CharField(max_length=7, min_length=0, required=False,
                               help_text='Enter ref code with 5 symbols of length or leave the field empty')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "ref_code"]

    def clean_ref_code(self):
        data = self.cleaned_data['ref_code']

        if len(data):
            try:
                ViralUser.objects.get(invite_code=data)
            except ViralUser.DoesNotExist:
                raise forms.ValidationError("Invalid ref code")
        return data

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        ref_code = self.cleaned_data['ref_code']
        if len(ref_code):
            profile = ViralUser.objects.get(invite_code=ref_code)
            profile.invited_users_amount += 1
            profile.save()

        if commit:
            user.save()

        return user


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ViralUser
        fields = ["description", ]
