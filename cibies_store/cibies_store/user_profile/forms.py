from django import forms
from cibies_store.products.models import Product
from cibies_store.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']

class ProfileCreateForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.label = ""

    class Meta(ProfileBaseForm.Meta):
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder':'Password',
                    'autocomplete': 'off',
                    'data-toggle': 'password'
                }
            ),  
        }

class ProfileEditForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['image_url'].label = "Image URL"
        self.fields['age'].label = "Age"
    
    class Meta(ProfileBaseForm.Meta):
        exclude = ['password', 'email']

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Product.objects.all().delete()
            Profile.objects.all().delete()
        return self.instance