from django import forms
from cibies_store.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCreateForm(ProductBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.label = ""

    class Meta(ProductBaseForm.Meta):
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Product Name'
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Product Image URL'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Product Description'
                }   
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Product Price'
                }
            ),
            'weight': forms.TextInput(
                attrs={
                    'placeholder': 'Product Weight'
                }
            )
        }

class ProductEditForm(ProductBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['image_url'].label = "Image URL"
        self.fields['description'].label = "Description"
        self.fields['price'].label = "Price"
        self.fields['weight'].label = "Weight"

class ProductDeleteForm(ProductBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance