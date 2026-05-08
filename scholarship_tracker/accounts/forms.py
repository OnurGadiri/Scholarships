from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_of_study = forms.CharField(
        max_length=150,
        required=False,
        label="Təhsil sahəsi",
    )
    target_country = forms.CharField(
        max_length=100,
        required=False,
        label="Hədəf ölkə",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            w = f.widget
            if isinstance(w, (forms.TextInput, forms.EmailInput, forms.PasswordInput)):
                w.attrs.setdefault("class", "inp")
            elif isinstance(w, forms.Textarea):
                w.attrs.setdefault("class", "inp")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            profile = user.profile
            profile.field_of_study = self.cleaned_data.get("field_of_study", "")
            profile.target_country = self.cleaned_data.get("target_country", "")
            profile.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("field_of_study", "target_country")
        labels = {
            "field_of_study": "Təhsil sahəsi",
            "target_country": "Hədəf ölkə",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "inp")
    